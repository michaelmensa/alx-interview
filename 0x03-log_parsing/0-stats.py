#!/usr/bin/python3
'''
Module Log parsing: script that reads stdin line by line and computes metrics:
'''
import sys
from collections import Counter


def process_line(line, file_sizes, status_codes):
    ''' function to process lines from stdin '''
    strip_line = line.strip()
    parsed_line = strip_line.split(' ')

    file_sizes.append(int(parsed_line[-1]))
    status_codes.append(int(parsed_line[-2]))


def print_metrics(file_sizes, status_codes):
    ''' prints metrics to the terminal '''
    if file_sizes:
        total_size = sum(file_sizes)
        print(f'File_size: {total_size}')

    occ = Counter(status_codes)
    for value, count in sorted(occ.items()):
        print(f'{value}: {count}')


def main():
    ''' reads line by line in stdin and return a list '''
    file_sizes = []
    status_codes = []

    try:
        for i, line in enumerate(sys.stdin, start=1):
            process_line(line, file_sizes, status_codes)

            if i % 10 == 0:
                print_metrics(file_sizes, status_codes)

    except KeyboardInterrupt:
        print_metrics(file_sizes, status_codes)


if __name__ == "__main__":
    main()
