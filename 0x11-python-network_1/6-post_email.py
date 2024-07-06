#!/usr/bin/python3
"""
Sends a POST request to a given URL with an email as a parameter and displays the response body.
Usage: ./6-post_email.py <URL> <email>
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    
    # Step 2: Prepare data to be sent as POST request
    data = {"email": email}
    
    # Step 3: Send a POST request using requests
    response = requests.post(url, data=data)
    
    # Step 4: Display the body of the response
    print(response.text)

