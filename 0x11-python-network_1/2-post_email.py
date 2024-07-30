#!/usr/bin/python3
"""
Sends a POST request to a given URL with a given email.
Usage: ./2-post_email.py <URL> <email>
  - Displays the body of the response.
"""
import sys
import urllib.parse
import urllib.request

if __name__ == "__main__":
    # Step 2: Get the URL and email from the command-line arguments
    url = sys.argv[1]
    value = {"email": sys.argv[2]}
    
    # Step 3: Encode the email parameter
    data = urllib.parse.urlencode(value).encode("ascii")
    
    # Step 4: Create a request object for the URL
    request = urllib.request.Request(url, data)
    
    # Step 5: Open the URL using a with statement
    with urllib.request.urlopen(request) as response:
        # Step 6: Read and decode the response body
        print(response.read().decode("utf-8"))

