#!/bin/bash
# Sends a request to a URL and displays only the status code of the response.

# Check if exactly one argument is provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send request with curl and output only the HTTP status code
curl -s -o /dev/null -w "%{http_code}" "$1"

