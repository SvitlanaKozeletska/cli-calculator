import argparse

def add(x: float, y: float) -> float:
    return x + y


def substract(x: float, y: float) -> float:
    return x - y


def divide(x: float, y: float) -> float:
    if y == 0:
        return 'Error: Division by zero'
    return x / y


def main():
    parser = argparse.ArgumentParser(
        description='A simple CLI calculator',
        usage='Specify the operation (\'add\', \'substract\' or \'divide\') and the two numbers to operate on'
        )
    
    # A positional argument that specifies the arithmetic operation.
    # It has a limited set of choices: 'add', 'substract', 'divide'
    parser.add_argument('operation', type=str, choices=['add', 'substract', 'divide'], help='The operation to perform')
    # A positional argument for the first number. It is expected to be a float
    parser.add_argument('x', type=float, help='The first number')
    # A positional argument for the second number. It is expected to be a float
    parser.add_argument('y', type=float, help='The second number')

    args = parser.parse_args()

    if args.operation == 'add':
        result = add(args.x, args.y)
    elif args.operation == 'substract':
        result = substract(args.x, args.y)
    elif args.operation == 'divide':
        result = divide(args.x, args.y)

    print(f'The result is: {result}')

if __name__ == "__main__":
    main()
