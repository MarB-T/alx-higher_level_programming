#!/usr/bin/python3
"""module docstring """
import sys

metrics = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}

total_file_size = 0
line_count = 0

try:
    for line in sys.stdin:
        line_count += 1

        _, _, _, _, status_code, file_size = line.split(' ')

        total_file_size += int(file_size)

        if status_code in metrics:
            metrics[status_code] += 1

        if line_count % 10 == 0:
            print(f'Total file size: {total_file_size}')

            for code, count in sorted(metrics.items()):
                if count > 0:
                    print(f'{code}: {count}')

except KeyboardInterrupt:
    print(f'Total file size: {total_file_size}')

    for code, count in sorted(metrics.items()):
        if count > 0:
            print(f'{code}: {count}')
