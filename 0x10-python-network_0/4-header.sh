#!/bin/bash
# Send GET request for a given url and include header with value 98
curl -sH "X-School-User-Id: 98" "$1"
