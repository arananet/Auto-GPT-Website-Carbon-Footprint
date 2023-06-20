from typing import Dict, Any, Optional
import os
import requests
import re
import json

def print_formatted_json(response: Dict[str, Any]) -> None:
    try:
        response_data = json.loads(response["response"])
        formatted_json = json.dumps(response_data, indent=4)
        print(formatted_json)
    except json.JSONDecodeError as e:
        print(f"Failed to parse the inner JSON: {e}")
        print(response)

def get_carbon_footprint(website: str, headers: Dict = {"Content-Type": "application/json"}, timeout_secs: int = 60) -> str:

	def sanitize_string(input_string: str) -> str:
		return re.sub(r'[^a-zA-Z0-9_: -{}[\],"]', '', input_string)

	def sanitize_json(input_string: str) -> str:
		data = json.loads(input_string)
		sanitized_data = {sanitize_string(k): sanitize_string(str(v)) for k, v in data.items()}
		return json.dumps(sanitized_data)

	def sanitize(input_string: str) -> str:
		try:
			sanitized_string = sanitize_json(input_string)
		except json.JSONDecodeError:
			sanitized_string = sanitize_string(input_string)
		return sanitized_string

	base_url = "https://api.websitecarbon.com"
	endpoint = os.getenv("WEBSITECARBON_ENDPOINT")

	if endpoint == "/site":
		request_url = f"{base_url}/site?url={website}"
	elif endpoint == "/data":
		bytes_value = input("Enter the bytes value: ")
		green_value = input("Enter 1 if powered by green hosting or 0 if not: ")
		request_url = f"{base_url}/data?bytes={bytes_value}&green={green_value}"
	else:
		print(f"Invalid WEBSITECARBON_ENDPOINT: {endpoint}")
		return json.dumps({"status": "error", "message": "Invalid WEBSITECARBON_ENDPOINT"})

	sanitized_url = sanitize(request_url)

	try:
		response = requests.get(sanitized_url, headers=headers, timeout=timeout_secs)
		response_text = response.text
		response = {
			"status": "success",
			"status_code": response.status_code,
			"response": response_text
		}

	except requests.exceptions.RequestException as e:
		response = {
			"status": "error",
			"status_code": None,
			"response": str(e)
		}

	if response:
		print_formatted_json(response)
		return {"status": "success", "response": response}
	else:
		print("An error occurred while fetching the carbon footprint.")
		return None

	#return json.dumps(response)