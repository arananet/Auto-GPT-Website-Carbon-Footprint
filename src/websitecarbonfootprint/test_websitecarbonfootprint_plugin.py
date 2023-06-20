import unittest
import os
from unittest.mock import patch
from websitecarbonfootprint_plugin import get_carbon_footprint


class TestCarbonFootPrint(unittest.TestCase):

    @patch("websitecarbonfootprint.get_carbon_footprint")
    def test_get_carbon_footprint_success(self, mock_requests_get):
        test_data = {"status": "success", "result": "test_result"}
        mock_requests_get.return_value.status_code = 200
        mock_requests_get.return_value.json.return_value = test_data

        os.environ["SUSTAINABILITY_ENDPOINT"] = "/site"

        result = get_carbon_footprint({"website": "https://example.com"})
        self.assertEqual(result, test_data)

    @patch("websitecarbonfootprint.get_carbon_footprint")
    def test_get_carbon_footprint_error(self, mock_requests_get):
        mock_requests_get.return_value.status_code = 400

        os.environ["SUSTAINABILITY_ENDPOINT"] = "/site"

        result = get_carbon_footprint({"website": "https://example.com"})
        self.assertFalse(result)

    def test_get_carbon_footprint_invalid_endpoint(self):
        os.environ["SUSTAINABILITY_ENDPOINT"] = "/invalid"

        result = get_carbon_footprint({"website": "https://example.com"})
        self.assertFalse(result)

    def test_get_carbon_footprint_no_website_in_params(self):
        os.environ["SUSTAINABILITY_ENDPOINT"] = "/site"

        result = get_carbon_footprint({"invalid_key": "https://example.com"})
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()