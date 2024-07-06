#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status."""
import urllib.request

if __name__ == "__main__":
    # Step 2: Create a request object for the URL
    request = urllib.request.Request("https://alx-intranet.hbtn.io/status")
    
    # Step 3: Open the URL using a with statement
    with urllib.request.urlopen(request) as response:
        # Step 4: Read the response body
        body = response.read()
        
        # Step 5: Display the response information
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))

