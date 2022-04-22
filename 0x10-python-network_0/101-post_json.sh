#!/bin/bash
# Must send a POST request with the contents of a file, passed with the filename as the second argument of the script, in the body of the request
curl -sH "Content-Type: application/json" -d @"$2" "$1"
