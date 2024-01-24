
Certainly! Here's a detailed description in markup form:

```markdown
# Rotate 2D Matrix

## Mandatory

Given an `n x n` 2D matrix, the task is to rotate it 90 degrees clockwise.

## Prototype

```python
def rotate_2d_matrix(matrix):
```

## Requirements

- **In-Place Editing**: The function must edit the matrix in-place, i.e., without creating a new matrix or using additional space.
- **No Return**: The function should not return anything.

## Input

- The input matrix will be a square matrix of size `n x n`.
- The matrix will have two dimensions.
- The matrix will not be empty.

## Approach

The goal is to rotate the matrix 90 degrees clockwise. To achieve this, each element in the matrix needs to be moved to a new position based on the clockwise rotation.

One possible approach is to perform the rotation in layers. Starting from the outermost layer and moving towards the center, swap the elements in a circular manner.

## Implementation

- Iterate through each layer of the matrix, starting from the outermost layer and moving towards the center.
- For each layer, iterate through the elements in a circular manner, swapping them with the corresponding elements in the clockwise direction.
- Continue this process until all layers have been rotated.

## Example

```python
# Example matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# After calling rotate_2d_matrix(matrix), the matrix will be rotated 90 degrees clockwise in-place:
# Resulting matrix:
# [
#    [7, 4, 1],
#    [8, 5, 2],
#    [9, 6, 3]
# ]
```

Remember to implement the function `rotate_2d_matrix` following the specified requirements.
```
