# FabSphinxExample

This is an example repo with fabric 1.x tasks mixed with sphinx-doc to generate
documentation. This was created during loose discussion on ##sublimetext
channel @ https://freenode.net

# Known limitations

- Ancient python, ancient fabric - tested under Ubuntu 16.04 with Python 2.7.x.
- There were not tries to make fabric tasks usable at all.


# Required packages

Under Ubuntu:
```bash
sudo apt-get install -y python-dev pandoc texlive-latex-base build-essential
```

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

# More info

See [fabric](https://github.com/fabric/fabric) and [sphinx-doc](http://www.sphinx-doc.org/en/master/).
