#!/bin/bash
# display all methods allowed for a URL
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
