import argparse

parser = argparse.ArgumentParser(
    prog='password-generator',
    description='Generate passwords and save them to storages'
)
parser.add_argument('--length', '-l', type=int, dest='length', nargs='?')
parser.add_argument('--platform', '-p', type=str, dest='platform', nargs='?')
parser.add_argument('--email', '-e', type=str, dest='email')
parser.add_argument('--login', '-lg', type=str, dest='login', nargs='?')
parser.add_argument('--storages', '-s', type=str, dest='storages', nargs='*')
parser.add_argument('--password', '-ps', type=str, dest='password', nargs='?')
parser.add_argument('--is_note', '-in', action='store_true', dest='is_note')
parser.add_argument('--is_digits', '-id', type=bool, dest='is_digits')
parser.add_argument('--is_capital_letters', '-ic', type=bool, dest='is_capital_letters')
parser.add_argument('--is_small_letters', '-is', type=bool, dest='is_small_letters')
parser.add_argument('--is_punctuation', '-ip', type=bool, dest='is_punctuation')


def get_arguments(argument_parser: argparse.ArgumentParser, args: list[str]) -> argparse.Namespace:
    return argument_parser.parse_args(args=args)
