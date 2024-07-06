#!/usr/bin/python3
"""
Sends a request to a given URL and displays the body of the response.
Manages HTTPError exceptions and prints error codes.
Usage: ./3-error_code.py <URL>
"""
import sys
import urllib.request
import urllib.error

if __name__ == "__main__":
    # Step 2: Get the URL from the command-line arguments
    url = sys.argv[1]
    
    # Step 3: Create a request object for the URL
    request = urllib.request.Request(url)
    
    try:
        # Step 4: Open the URL using a with statement and handle exceptions
        with urllib.request.urlopen(request) as response:
            # Step 5: Read and decode the response body
            body = response.read().decode("utf-8")
            print(body)
    except urllib.error.HTTPError as e:
        # Step 4: Print the error code if an HTTPError occurs
        print(f"Error code: {e.code}")

