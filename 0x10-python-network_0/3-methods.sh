#!/bin/bash
# This script sends an OPTIONS request to a URL and displays all HTTP methods the server will accept.
curl -sI -X OPTIONS "$1" | grep "Allow" | cut -d' ' -f 2-
