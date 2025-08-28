import importlib.metadata

# Get version from package metadata
try:
    __version__ = importlib.metadata.metadata('todocli')['Version']
except importlib.metadata.PackageNotFoundError:
    __version__ = "0.1.0.dev0"
