# todocli

A simple todo list application that can be used from the command line.

This application is used for
the [learnjj.codeandbugs.com](https://learnjj.codeandbugs.com) tutorial, to
teach using the Ju Jutsu (jj) version control system.

todocli is probably not very useful for anything else.

## Dev Setup

**Note:** If you are following the learnjj tutorial, you don't need to install
Poetry etc. You don't even need Python. It just means you won't be able to run
the _todocli_ application, but since you are only trying to learn jj, that's
probably not a problem.

### Prerequisites

* Make sure you have Python installed.
  Check [Python for Beginners](https://www.python.org/about/gettingstarted/).
* [Install Poetry](https://python-poetry.org/docs/#installation)

Clone the repository:

```bash
git clone https://github.com/omarkohl/jj-tutorial.git
cd jj-tutorial
```

Set up the virtual environment:

```bash
poetry install
```

Try the application:

```bash
poetry run todocli --version
```
