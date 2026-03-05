## Math CLI

This project is a simple proof-of-concept Python CLI that performs basic math operations.

### Available math methods

- **`add_numbers(a, b)`**  
  - **Description**: Returns the sum of two numbers.  
  - **Signature**: `add_numbers(a: float, b: float) -> float`  
  - **Defined in**: `math_cli.py`  

### CLI usage

The CLI currently exposes the `add_numbers` function via command-line arguments.

```bash
python math_cli.py <a> <b>
```

Where:

- `a`: first number (parsed as float)
- `b`: second number (parsed as float)

The program prints the result of `add_numbers(a, b)` to standard output.
