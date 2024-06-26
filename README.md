# Overview
The purpose of this repository is to demystify the simplicity of passing an image via an API call and receiving a response. This basic principle of querying AI using images can be extrapolated to a wide range of solutions, empowering our Salesforce KADS, AEs, Solution Engineers and more to think beyond standard out-of-the-box capabilities.

#### Key Objectives:
**Understanding API Image Processing:** Demonstrates how to send an image to an AI service and receive a response, providing a foundational understanding of image-based AI interactions.

**Expanding Solution Engineering Horizons:** Encourages solution engineers to explore innovative solutions by leveraging AI technology, thus enabling more comprehensive and creative customer solutions.

**Practical Applications:** Offers practical insights into how this technology can be integrated into various use cases, providing real-world examples to inspire further innovation.

#### Vision:
By mastering this fundamental concept, KADs, AEs, Solution Engineers and more at Salesforce can significantly enhance their problem-solving toolkit. This approach not only broadens their technical repertoire but also equips them with the knowledge to propose and implement more versatile and robust solutions for customers. 

The ultimate goal is to inspire a mindset that consistently seeks out novel and effective applications of AI technology in addressing customer needs.

------------

# Instructions

### Download and intall python if you don`t have it. Otherwise skip this step
**1. Open terminsal and Install Brew (package Manager)**

    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)" 

**2. Install Python**

    brew install python

**3. Check Python Version. Make sure it`s installed **

    python3 --version


------------


### Download and install Visual Studio Code. Otherwise skip this step

https://code.visualstudio.com/

------------

### Clone repo and open

1. Clone this repo then open the repo folder in VSC

------------
### Open a terminal in VSC
Run the following commands

    python3 -m venv .venv
    . .venv/bin/activate
    source .venv/bin/activate
    pip3 install openai pillow aiohttp

### Go to OpenAI ande Generate a API KEY
1. https://www.youtube.com/watch?v=gBSh9JI28UQ
2. Put the OpenAI Key into the code where is says:


        OPENAI_API_KEY = "put_open_ai_key_here" 

I have porovded an image called "integrated_service.png" that is a screenshot of a Salesforce page.


------------

### Run the script
Simply run the script then by typing:


    python3 vision_llm_example.py  

### Output
The output you get should be:

> {'description': 'The image provided is a sample dashboard from a Client Relationship Management (CRM) system. The dashboard is titled "Client Solutions" and appears to focus on key metrics related to client interactions, activities, revenue, and pipeline. Here’s a breakdown of the different sections and data visualizations shown:\n\n### Top Menu\n- **Client Solutions**: The main title of the dashboard.\n- **Home, Onboarding, Research, News**: Navigation tabs at the top.\n\n### Main Sections\n1. **Activity & Pipeline**\n    - **Revenue**: Displays the current month\'s, quarter\'s, and fiscal year\'s revenue ($9.31M, $33.3M, $70.5M).\n    - **Clients**: Displays the number of clients (10).\n    - **Interactions**: Displays the number of interactions (2,881).\n    - **Pipeline**: Displays the current pipeline value ($2.5B).\n    - **Campaign**: Displays the number of campaigns (4.5k).\n\n2. **Revenue and Activities by Tier**\n    - Pie chart visualizing the count of activities by tier (Tier 1, Tier 2, Tier 3).\n    - Line and bar chart showing the trend of revenue and activities over several months (May to October).\n    - Bar and vertical line chart representing revenue and sum of activities by account and vertical.\n\n3. **Today’s Events**\n    - Lists scheduled events with times:\n        - 3:30 AM:'}

##### You can now test out different images and experiement.


Ping me at malcolm.fitzgerald@salesforce.com is you run into any issues.

