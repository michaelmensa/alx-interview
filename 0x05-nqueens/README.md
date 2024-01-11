l of the program is to solve the N queens problem and print every possible solution to the problem.

## Usage

The program is invoked from the command line using the following syntax:

```bash
nqueens N
```

- If the user calls the program with the wrong Here's a detailed description of the specified program in markup form:

```markdown
# N Queens Solver

## Description

The N queens puzzle is a classic chess problem where the challenge is to place N non-attacking queens on an NxN chessboard. The gonumber of arguments, the program should print:
  ```bash
  Usage: nqueens N
  ```
  followed by a new line, and exit with the status 1.

- The value of N must be an integer greater than or equal to 4. If the provided N is not an integer, the program should print:
  ```bash
  N must be a number
  ```
  followed by a new line, and exit with the status 1.

- If N is smaller than 4, the program should print:
  ```bash
  N must be at least 4
  ```
  followed by a new line, and exit with the status 1.

## Output

The program should print every possible solution to the N queens problem. Each solution should be printed on a new line. The format for each solution should follow the example format.

## Example

Suppose the program is called with the following command:

```bash
nqueens 4
```

The program should then print:

```
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
```

Note: The order of the solutions does not need to be specific.

## Constraints

- The program is only allowed to import the sys module.
```

This markup provides a detailed description of the program's functionality, usage, and expected output, making it easier for users to understand and interact with the N Queens Solver.
