Certainly! Here is the detailed description in markup form:

```plaintext
## Problem: Making Change

Given a pile of coins of different values, the task is to determine the fewest number of coins needed to meet a given total amount.

### Prototype
```python
def makeChange(coins, total):
    """Return the fewest number of coins needed to meet the total amount."""
```

### Return
- The function should return the fewest number of coins needed to meet the total amount.

### Conditions
- If the total amount is 0 or less, the function should return 0.
- If the total amount cannot be met by any combination of coins in your possession, return -1.

### Parameters
- `coins`: A list of values representing the denominations of the coins in your possession.
- `total`: The total amount that needs to be achieved using the available coins.

### Constraints
- The value of each coin is always an integer greater than 0.
- You can assume that you have an infinite number of each denomination of coin in the list.

### Evaluation
- The performance of your solution, particularly its runtime, will be evaluated in this task.
```
