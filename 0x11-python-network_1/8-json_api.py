#!/usr/bin/python3
"""
Sends a POST request to http://0.0.0.0:5000/search_user with a given letter.
Usage: ./8-json_api.py <letter>
  - The letter is sent as the value of the variable `q`.
  - If no letter is provided, sends `q=""`.
"""
import sys
import requests

if __name__ == "__main__":
    # Determine the letter from command-line arguments
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    
    # Prepare POST data
    payload = {"q": letter}
    
    # Send POST request
    r = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    
    try:
        # Attempt to parse response as JSON
        response = r.json()
        
        # Check if response is empty
        if not response:
            print("No result")
        else:
            # Print id and name from JSON response
            print("[{}] {}".format(response.get("id"), response.get("name")))
    
    except ValueError:
        # Handle invalid JSON response
        print("Not a valid JSON")

