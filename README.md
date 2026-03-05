## Math CLI

This project is a simple proof-of-concept Python CLI that performs basic math operations.

### Available math methods

- **`add_numbers(a, b)`**  
  - **Description**: Returns the sum of two numbers.  
  - **Signature**: `add_numbers(a: float, b: float) -> float`  
  - **Defined in**: `math_cli.py`  
  
- **`multiply_numbers(a, b)`**  
  - **Description**: Returns the product of two numbers.  
  - **Signature**: `multiply_numbers(a: float, b: float) -> float`  
  - **Defined in**: `math_cli.py`  

### CLI usage

The CLI exposes these operations via subcommands:

- `sum`: calls `add_numbers(a, b)`
- `multiply`: calls `multiply_numbers(a, b)`

```bash
# Add two numbers
python math_cli.py sum <a> <b>

# Multiply two numbers
python math_cli.py multiply <a> <b>
```

Where:

- `a`: first number (parsed as float)
- `b`: second number (parsed as float)

The program prints the numeric result of the selected operation to standard output.
