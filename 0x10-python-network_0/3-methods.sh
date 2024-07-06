#!/bin/bash
# This script sends an OPTIONS request to a URL and displays all HTTP methods the server will accept.

# Send the OPTIONS request and extract the Allow header
methods=$(curl -sI -X OPTIONS "$1" | grep "Allow:" | cut -d' ' -f2-)

# Print the allowed methods
echo "$methods"

