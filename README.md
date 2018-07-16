# Required packages

Under ubuntu:
sudo apt-get install -y python-dev pandoc texlive-latex-base build-essential

# Docs generation

## Basic usage:

Python 2.7.x

```bash
virtualenv .venv/
source .venv/bin/activate
pip install -r requirements.txt

make apidoc
make html
```

## More advanced usage:

- Docs sources are in `source`, see `conf.py` for more details.
- Makefile targets - see `make help`, but notice that some are hidden (for example `apidoc`)
- Output is in `build/<target>`
