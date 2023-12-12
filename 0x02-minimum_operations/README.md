# Minimum Operations

## Problem Description

In a text file, there is a single character H. Your text editor can execute only two operations in this file: Copy All and Paste. Given a number `n`, write a method that calculates the fewest number of operations needed to result in exactly `n` H characters in the file.

## Prototype

```python
def minOperations(n: int) -> int:
    """
    Calculate the fewest number of operations needed to obtain exactly n H characters.

    Parameters:
    - n (int): The target number of H characters.

    Returns:
    - int: The minimum number of operations needed. If n is impossible to achieve, return 0.
    """
    pass
```

## Example

```python
n = 9
result = minOperations(n)
# Result: 6
```

## Explanation

For the given example:

- Initial state: H
- Operation 1: Copy All (H)
- Operation 2: Paste (HH)
- Operation 3: Paste (HHH)
- Operation 4: Copy All (HHH)
- Operation 5: Paste (HHHHHH)
- Operation 6: Paste (HHHHHHHHHH)

The minimum number of operations to obtain 9 H characters is 6.

## Notes

- The method should handle cases where it is impossible to achieve the target number `n` and return 0 in such cases.
- The provided prototype indicates the function signature, and the implementation should adhere to it.
