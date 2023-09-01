#!/bin/bash
# returns status code
curl -s -o /de/null -w "%{http_code}" "$1"
