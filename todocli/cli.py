import sys
import os
from .__version__ import __version__

def version():
    app_name = "todocli"
    print(f"{app_name} {__version__}")


def help():
    print("Usage: todocli [OPTIONS] COMMAND [ARGS]...")
    print("Options:")
    print("  -v, --version  Show the version and exit.")
    print("  -h, --help     Show this message and exit.")
    print("Commands:")
    print("  help          Show this message and exit.")


def cli():
    if len(sys.argv) > 1:
        if sys.argv[1] in ("-v", "--version"):
            version()
            return
        elif sys.argv[1] in ("-h", "help", "--help"):
            help()
            return
        else:
            print("Unknown command")
            sys.exit(1)
    print("Hello, World!")
