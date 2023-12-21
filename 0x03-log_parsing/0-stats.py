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


"""
def main():
    ''' reads line by line in stdin and return a list '''
    file_sizes = []
    status_codes = []
    count = 0

    try:
        for line in sys.stdin:
            count += 1
            process_line(line, file_sizes, status_codes)

            if count % 10 == 0:
                print_metrics(file_sizes, status_codes)

    except KeyboardInterrupt:
        print_metrics(file_sizes, status_codes)
        raise
"""

if __name__ == "__main__":
    file_sizes = []
    status_codes = []
    count = 0

    try:
        for line in sys.stdin:
            count += 1
            process_line(line, file_sizes, status_codes)

            if count % 10 == 0:
                print_metrics(file_sizes, status_codes)
    finally:
        try:
            print_metrics(file_sizes, status_codes)
            raise KeyboardInterrupt
        except:
            pass
