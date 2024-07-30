#!/usr/bin/python3
"""
Sends a GET request to a given URL and displays the body of the response.
If HTTP status code is >= 400, prints an error message.
Usage: ./7-error_code.py <URL>
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    
    # Step 2: Send a GET request using requests
    response = requests.get(url)
    
    # Step 3: Display the body of the response
    print(response.text)
    
    # Step 4: Check HTTP status code and print error if >= 400
    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")

