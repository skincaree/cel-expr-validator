import argparse
import logging
from cel import Interpreter

def parse_args():
    """
    Parse command line arguments.

    Returns:
        argparse.Namespace: Parsed arguments.
    """
    parser = argparse.ArgumentParser(description='CEL Expression Validator')
    parser.add_argument('expr', help='CEL expression to validate')
    parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose logging')
    return parser.parse_args()

def validate_expr(expr):
    """
    Validate a CEL expression.

    Args:
        expr (str): CEL expression to validate.

    Returns:
        bool: True if the expression is valid, False otherwise.
    """
    try:
        interpreter = Interpreter()
        interpreter.evaluate(expr)
        return True
    except Exception as e:
        logging.error(f'Validation failed: {e}')
        return False

def main():
    """
    Main entry point.
    """
    args = parse_args()
    if args.verbose:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)

    logging.info(f'Validating expression: {args.expr}')
    if validate_expr(args.expr):
        logging.info('Expression is valid')
    else:
        logging.error('Expression is invalid')

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        logging.error(f'Error: {e}')
        exit(1)