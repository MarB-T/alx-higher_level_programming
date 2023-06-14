#!/usr/bin/python3
""" module docstring """


import sys
from collections import defaultdict

# Variables to hold metrics
file_sizes = []
status_counts = defaultdict(int)
line_count = 0

try:
    for line in sys.stdin:
        # Split the line into components
        parts = line.strip().split()
        if len(parts) >= 9:
            # Extract the file size and status code
            file_size = int(parts[-1])
            status_code = parts[-2]

            # Update metrics
            file_sizes.append(file_size)
            status_counts[status_code] += 1
            line_count += 1

        # Print statistics every 10 lines
        if line_count % 10 == 0:
            print("File size: ", sum(file_sizes))
            for status_code in sorted(status_counts):
                print(status_code + ":", status_counts[status_code])
except KeyboardInterrupt:
    # Print final statistics upon keyboard interruption
    print("File size: ", sum(file_sizes))
    for status_code in sorted(status_counts):
        print(status_code + ":", status_counts[status_code])
