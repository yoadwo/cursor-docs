---
name: cli-math
description: Describe how to perform math operations using this project's Python CLI, starting with adding two numbers. Use when the user asks how to run math commands via the CLI or how to extend the CLI with additional math operations.
---

# How to do math using the CLI

This skill explains how to use the Python CLI in this repository to perform math operations.  
Currently, the CLI supports adding two numbers via the `add_numbers` function in `math_cli.py`.

## Instructions

1. **Locate the CLI script**  
   - The main entry point is `math_cli.py` in the project root.

2. **Understand the core math function**  
   - Function: `add_numbers(a: float, b: float) -> float`  
   - Behavior: Returns the sum of its two arguments.  
   - This function contains all the math logic; the CLI only parses arguments and prints the result.

3. **Run the CLI to add two numbers**  
   - From the project root, run:
     - On most systems:
       - `python math_cli.py <a> <b>`
     - If `python` maps to Python 2, use:
       - `python3 math_cli.py <a> <b>`
   - Replace `<a>` and `<b>` with numeric values (integers or floats).  
   - The CLI parses both as `float`, calls `add_numbers(a, b)`, and prints the numeric result to standard output.

4. **Handling input types and errors**  
   - Non-numeric input (e.g., `"abc"`) will cause argument parsing to fail and exit with an error message from `argparse`.  
   - Whitespace and typical shell quoting rules follow your shell's behavior; pass each number as a separate argument.

5. **Extending the CLI with more math operations (future)**  
   - When adding new operations (e.g., subtraction, multiplication, division):
     - Implement each operation in a separate pure function (e.g., `subtract_numbers(a, b)`).
     - Keep CLI parsing and math logic separated: the CLI should parse arguments, select the operation, call the appropriate function, and print the result.
     - Update this skill file to document the new functions, their signatures, and example CLI invocations.

## Examples

- **Add two integers**
  - Command: `python math_cli.py 2 5`
  - Internal call: `add_numbers(2.0, 5.0)`
  - Output: `7.0`

- **Add two floating-point numbers**
  - Command: `python math_cli.py 3.5 4.25`
  - Internal call: `add_numbers(3.5, 4.25)`
  - Output: `7.75`

- **Add a negative and a positive number**
  - Command: `python math_cli.py -2 10`
  - Internal call: `add_numbers(-2.0, 10.0)`
  - Output: `8.0`

