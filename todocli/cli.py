import sys


def version():
    print("0.1.0")


def cli():
    if len(sys.argv) > 1:
        if sys.argv[1] == "--version":
            version()
            return
    print("Hello, World!")


if __name__ == "__main__":
    cli()
