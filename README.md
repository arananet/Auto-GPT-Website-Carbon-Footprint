# Auto-GPT Website-Carbon-Footprint Plugin: Take advantage of the Website Carbon Footprint API with Auto-GPT 🚀

Welcome to **Auto-GPT Website Carbon Footprint** – an innovative solution designed to detect website energy consumption and help stakeholders to reduce the carbon footprint of your online presence by using the https://api.websitecarbon.com/. In today's environmentally conscious world, it's more important than ever to keep our websites sustainable and energy-efficient. By using this plugin, you can play a pivotal role in counteracting climate change and creating a greener future for all.

## Introduction: The Importance of Website Carbon Footprint

Traditional web development methologies often do not prioritize energy efficiency. As a result, web pages can consume a considerable amount of energy, generate excessive data transfers, and contribute to data center carbon emissions. The combined impact of millions of such websites contributes significantly to global energy consumption and environmental degradation.

In recent years, the importance of assessing and reducing the carbon footprint of digital services, like websites, has become much more apparent. This understanding has grown as more people recognize the need for sustainable practices across all aspects of life.

The **Website Carbon Footprint** is a measure of the energy consumed by a website, including the processing of data transmitted over the Internet. A website using energy-efficient technologies and best practices can significantly reduce its carbon footprint, leading to increased sustainability both for the website and for the environment.

## About Auto-GPT Plugin

The **Auto-GPT Website Carbon Footprint** aims to:

1. Measure the carbon footprint of your website by analyzing its performance, design elements, and server operations.
2. Helps to identify the current values and how you should, based on the returned information to, fix or improve your website code.

Developed by Eduardo Arana in 2023 for the Auto-GPT project. This plugin is not affiliated with or endorsed by the Website Carbon Footprint company.

### Key Features and Benefits

- **Optimization Recommendations:** Based on the Website Carbon Footprint API analysis, the plugin will return values like:
  - green (if its considered a green website)
  - cleanerThan (an average compared with other websites)
  - energy (average of consumed energy)
  - co2 in grams and which portion.
  - if hosting is using renewable energy.

## 🔧 Installation

Follow these steps to configure the Auto-GPT Website Carbon Footprint:

### 1. Clone the Auto-GPT Website Carbon Footprint repository
Clone this repository and navigate to the `Auto-GPT-Website-Carbon-Footprint` folder in your terminal:

```bash
git clone https://github.com/arananet/Auto-GPT-Website-Carbon-Footprint.git
```

### 2. Install required dependencies
Execute the following command to install the necessary dependencies:

```bash
pip install -r requirements.txt
```

### 3. Package the plugin as a Zip file
Compress the `Auto-GPT-Website-Carbon-Footprint` folder or [download the repository as a zip file](https://github.com/arananet/Auto-GPT-Website-Carbon-Footprint/archive/refs/heads/master.zip).

### 4. Install Auto-GPT
If you haven't already, clone the [Auto-GPT](https://github.com/Significant-Gravitas/Auto-GPT) repository, follow its installation instructions, and navigate to the `Auto-GPT` folder.

### 5. Copy the Zip file into the Auto-GPT Plugin folder
Transfer the zip file from step 3 into the `plugins` subfolder within the `Auto-GPT` repo.

### 6. Locate the `.env.template` file
Find the file named `.env.template` in the main `/Auto-GPT` folder.

### 7. Create and rename a copy of the file
Duplicate the `.env.template` file and rename the copy to `.env` inside the `/Auto-GPT` folder.

### 8. Edit the `.env` file
Open the `.env` file in a text editor. Note: Files starting with a dot might be hidden by your operating system.

### 9. Add the Website Carbon Footprint API configuration
Append the following configuration settings to the end of the file:

```ini
################################################################################
### Auto-GPT Website Carbon Footprint
################################################################################

#/site or /data allowed endpoints, see plugin README.md for detailed explanation.
WEBSITECARBON_ENDPOINT=
```

1. **Website Carbon Footprint Api Endpoint:**
    - Set `WEBSITECARBON_ENDPOINT` there are two endpoints to that can be consumed from api.websitecarbon.com, 
    - /site = This endpoint requires a URL parameter and will run a test in real time to calculate the carbon emissions generated per page view.
    - /data = An endpoint to calculate the emissions of a page by manually passing the bytes and whether or not it is powered by green hosting.

    [More information, here](https://api.websitecarbon.com/).


### 10. Allowlist Plugin
In your `.env` search for `ALLOWLISTED_PLUGINS` and add this Plugin:

```ini
################################################################################
### ALLOWLISTED PLUGINS
################################################################################

#ALLOWLISTED_PLUGINS - Sets the listed plugins that are allowed (Example: plugin1,plugin2,plugin3)
ALLOWLISTED_PLUGINS=AutoGPTWebsiteCarbonFootprintPlugin
```

## 🧪 Test the Auto-GPT Website Carbon Footprint

Experience the plugin's capabilities by testing it to obtain the carbon emissions originated by an specific website or online service.

### 📤 Test Checking a Website

1. **Configure Auto-GPT:**
   Set up Auto-GPT with the following parameters:
   - Name: `Website carbon footprint GPT`
   - Role: `Obtain the carbon footprint emissions from a specific website's energy consumption and reduce the carbon footprint of your online presence. `
   - Goals:
     1. Goal 1: `Check the website https://bellymelter.com to retrieve the carbon emissions generated.`
     2. Goal 2: `Terminate`

2. **Run Auto-GPT:**
   Launch Auto-GPT, which should use the Auto-GPT Website Carbon Footprint to retrieve the carbon footprint values from an specific website.

3. **Output example:**
   <img width="800" alt="Auto-GPT-Website-Carbon-Footprint" src="https://github.com/arananet/Auto-GPT-Website-Carbon-Footprint/blob/main/output.png?raw=true">
