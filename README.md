# WeChat-Auto-Responder-Based-on-Tencent-Cloud-Platform
This Python application serves as an automated response handler for a WeChat Official Account. It processes incoming messages using HTTP methods (GET for verification and POST for message handling) and responds appropriately based on the type of the message received (text, image, voice, event).

Here's a README file for the provided Python script. It includes an overview of the script's functionality, how to set it up, and details about the external dependencies and local module imports.

---

## Features

- **Verification with WeChat Server**: Uses GET requests to validate the server.
- **Automatic Reply to Subscriptions**: Sends a welcome message when a user subscribes.
- **Text Message Responses**: Can reply with text, fetch data from a local dictionary, or search through CNKI.
- **Image Message Handling**: Replies with the media ID of received images.
- **Voice Message Recognition**: Processes recognized text from voice messages and searches for responses.
- **QR Code Response**: Sends a QR code image upon specific text commands.

## Prerequisites

Ensure you have Python installed on your system. This script is compatible with Python 3.x.

### Dependencies

- `requests`: For sending HTTP requests.
- `BeautifulSoup4`: For parsing HTML/XML content.
- `json`: For JSON parsing.
- `hashlib`: For generating hash values.
- `time`: For accessing and manipulating times.
- `reply`: A local module for constructing and sending reply messages.
- `xml.etree.ElementTree`: For XML parsing.

To install the required Python packages, run:
```bash
pip install requests beautifulsoup4
```

### Local Module Imports

- `dic_search`: A function from the local file `dic_search.py` that performs searches in a local dictionary.
- `cnki_search`: A function from the local file `cnkisearch.py` that performs searches via the CNKI database.

## Setup

1. **Local Configuration**:
   - Ensure all local Python files (`dic_search.py` and `cnkisearch.py`) are in the same directory as the main script.
   - Store any necessary text files (like `AutoReplyContent.txt` for subscription messages) and media (like `qrcode.jpg` for QR code responses) in the same directory or specify the path in the script.

2. **WeChat Configuration**:
   - Configure your WeChat official account to interact with the endpoint where this script is hosted.
   - Set up appropriate URL and Token on WeChat to match the script verification phase.

## Running the Script

To execute the script, simply run:
```bash
python your_script_name.py
```
Ensure that this script is hosted on a server that can interact with WeChat's servers to receive and send messages.

## Example Usage

```python
event = {
    'httpMethod': 'POST',
    'body': '<xml data here>'
}
context = {}

response = main_handler(event, context)
print(response)
```

This example illustrates how to manually test the `main_handler` function with predefined `event` and `context`.

## Note

Ensure that the environment where this script is running is secure and configured correctly to handle web requests, especially if exposed to the public internet. This script assumes a server-side environment where Python is used to handle HTTP requests and responses. Adjust firewall and server settings accordingly to avoid unauthorized access.

---

This README aims to provide a comprehensive guide for setting up and running the provided Python script effectively. Adjust the content to fit any additional configurations or environment specifics relevant to your deployment scenario.
