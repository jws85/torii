import sys
from torii.generate import generate

def run():
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} JINJA2-FILE JSON-FILE")
        print()
        print("This program populates a Jinja2 template file with values from a JSON file.")
        print("It may be useful, for instance, when a program's configuration format is not")
        print("expressive enough for your needs.")
        sys.exit(1)

    try:
        print(generate(sys.argv[1], sys.argv[2]))
    except FileNotFoundError as err:
        print('File not found: ' + str(err))
        sys.exit(2)
