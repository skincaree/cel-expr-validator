# CEL Expression Validator
A validation tool for Google's CEL (Common Expression Language) expressions in Python, providing a safe and typed way to evaluate expressions and prevent potential security vulnerabilities.

## Features
* Validate CEL expressions using the `cel` library
* Support for verbose logging
* Command line interface with `--help` option

## Installation
To install the CEL Expression Validator, run the following command:
```bash
pip install -r requirements.txt
```
## Usage
To validate a CEL expression, run the following command:
```bash
python main.py '1 + 2 * 3'
```
This will validate the expression `1 + 2 * 3` and print a success message if the expression is valid.

To enable verbose logging, use the `-v` or `--verbose` option:
```bash
python main.py -v '1 + 2 * 3'
```
This will print detailed logging information during the validation process.

## License
The CEL Expression Validator is licensed under the MIT License. See the LICENSE file for details.