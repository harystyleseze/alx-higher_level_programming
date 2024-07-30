#!/usr/bin/python3
"""
Displays the X-Request-Id header variable of a request to a given URL.
Usage: ./1-hbtn_header.py <URL>
"""
import sys
import urllib.request

if __name__ == "__main__":
    # Get the URL from the command-line arguments
    url = sys.argv[1]

    # Create a request object for the URL
    request = urllib.request.Request(url)

    # Open the URL using a with statement
    with urllib.request.urlopen(request) as response:
        # Convert headers to a dictionary and get the value of X-Request-Id
        print(dict(response.headers).get("X-Request-Id"))

