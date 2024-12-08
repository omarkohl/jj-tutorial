import sys
from .__version__ import __version__

def version():
    print(f"todocli {__version__}")


def cli():
    if len(sys.argv) > 1:
        if sys.argv[1] == "--version":
            version()
            return
    print("Hello, World!")
