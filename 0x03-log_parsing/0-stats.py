#!/usr/bin/python3
'''
Module Log parsing: script that reads stdin line by line and computes metrics:
'''
import sys
from collections import Counter


def main():
    ''' reads line by line in stdin and return a list '''
    stats = []
    file_size = []
    status_code = []
    stats.append(file_size)
    stats.append(status_code)
    lines = 0

    try:
        for line in sys.stdin:
            lines += 1
            strip_line = line.strip()
            parsed_line = strip_line.split(' ')

            file_size.append(int(parsed_line[-1]))
            status_code.append(int(parsed_line[-2]))

            if lines % 10 == 0:
                if len(file_size) > 0:
                    total_size = sum(file_size)
                    print(f'File_size: {total_size}')

                occ = Counter(status_code)
                for value, count in sorted(occ.items()):
                    print(f'{value}: {count}')

    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()
