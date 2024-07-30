#!/usr/bin/python3
"""
Fetches https://alx-intranet.hbtn.io/status using the requests package.
Displays the body of the response in a specific format.
"""
import requests

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    
    # Step 2: Send a GET request using requests
    response = requests.get(url)
    
    # Step 3: Access the response content
    content = response.text
    
    # Step 4: Display the response in the required format
    print("Body response:")
    print(f"\t- type: {type(content)}")
    print(f"\t- content: {content}")

