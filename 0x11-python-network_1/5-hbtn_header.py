#!/usr/bin/python3
"""
Sends a request to a given URL and displays the value of the X-Request-Id header variable.
Usage: ./5-hbtn_header.py <URL>
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    
    # Step 2: Send a GET request using requests
    response = requests.get(url)
    
    # Step 3: Access the X-Request-Id header and display its value
    request_id = response.headers.get('X-Request-Id')
    print(request_id)

