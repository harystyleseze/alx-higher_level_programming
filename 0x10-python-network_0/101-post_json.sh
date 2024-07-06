#!/bin/bash
# Sends a JSON POST request to a URL and displays the body of the response.

# Check if exactly two arguments are provided
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <URL> <JSON filename>"
    exit 1
fi

# Assign arguments to variables
URL="$1"
JSON_FILE="$2"

# Check if the JSON file exists and is readable
if [ ! -f "$JSON_FILE" ] || [ ! -r "$JSON_FILE" ]; then
    echo "Error: JSON file '$JSON_FILE' not found or not readable."
    exit 1
fi

# Check if the JSON file is valid JSON
if ! jq empty < "$JSON_FILE" > /dev/null 2>&1; then
    echo "Error: '$JSON_FILE' is not a valid JSON file."
    exit 1
fi

# Send POST request with curl
curl -s -X POST -H "Content-Type: application/json" -d @"$JSON_FILE" "$URL"

