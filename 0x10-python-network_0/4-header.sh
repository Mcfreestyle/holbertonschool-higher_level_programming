#!/bin/bash
# Sends a GET request to the URL, and displays the body of the response, a header variable X-School-User-Id must be sent with the value 98
curl -sH 'X-School-User-Id: 98' "$1"
