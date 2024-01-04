#!/usr/bin/python3
''' Module 0-validate_utf8: utf-8 validation '''


def validUTF8(data):
    ''' Variable to track the number of bytes remaining for the current
    character'''
    remaining_bytes = 0
    # Iterate through each byte in the data
    for byte in data:
        # Check if it's a continuation byte (starts with 10xxxxxx)
        if remaining_bytes > 0 and (byte & 0b11000000) == 0b10000000:
            remaining_bytes -= 1
        elif remaining_bytes == 0:
            # Determine the number of bytes for the current character
            if (byte & 0b10000000) == 0:  # 1-byte character
                remaining_bytes = 0
            elif (byte & 0b11100000) == 0b11000000:  # 2-byte character
                remaining_bytes = 1
            elif (byte & 0b11110000) == 0b11100000:  # 3-byte character
                remaining_bytes = 2
            elif (byte & 0b11111000) == 0b11110000:  # 4-byte character
                remaining_bytes = 3
            else:
                # Invalid start byte
                return False
        else:
            # Invalid continuation byte
            return False

    # If there are remaining bytes after iterating through all data,
    # it's invalid
    return remaining_bytes == 0
