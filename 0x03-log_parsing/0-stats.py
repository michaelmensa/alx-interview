#!/usr/bin/python3
'''
Module Log parsing: script that reads stdin line by line and computes metrics:
'''
import sys


if __name__ == "__main__":
    file_sizes = [0]
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0,
                    404: 0, 405: 0, 500: 0}
    count = 0

    def print_metrics():
        ''' prints metrics to the terminal '''
        print(f'File_size: {file_sizes[0]}')

        for key in sorted(status_codes.keys()):
            if status_codes[key]:
                print(f'{key}: {status_codes[key]}')

    try:
        for line in sys.stdin:
            count += 1

            parsed_line = line.split(' ')

            try:
                file_size = int(parsed_line[-1])
                status_code = int(parsed_line[-2])
            except Exception:
                pass

            file_sizes[0] += file_size
            if status_code in status_codes:
                status_codes[status_code] += 1

            if count % 10 == 0:
                print_metrics()
        print_metrics()
    except KeyboardInterrupt:
        print_metrics()
        raise
