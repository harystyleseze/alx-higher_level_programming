#!/usr/bin/python3
"""Uses the GitHub API to display a GitHub ID based on given credentials.
Usage: ./10-my_github.py <GitHub username> <GitHub password>
  - Uses Basic Authentication to access the ID.
"""
import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    # Ensure that exactly two command-line arguments are provided
    if len(sys.argv) != 3:
        print("Usage: ./10-my_github.py <GitHub username> <GitHub password>")
        sys.exit(1)

    # Extract username and token from command-line arguments
    username = sys.argv[1]
    token = sys.argv[2]

    # Create Basic Authentication object
    auth = HTTPBasicAuth(username, token)

    try:
        # Send GET request to GitHub API
        response = requests.get("https://api.github.com/user", auth=auth)

        # Check if the response is successful
        if response.status_code == 200:
            # Parse JSON response and print the user ID
            user_data = response.json()
            print(user_data.get("id"))
        else:
            # Print None for unsuccessful responses
            print("None")
    except requests.RequestException as e:
        # Handle network errors and other request-related errors
        print("None")

