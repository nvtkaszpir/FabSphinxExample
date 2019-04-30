# FabSphinxExample

# Notice

This repo is deadand will not be updated to python3.

I suggest swithich go invoke which is a succesor of fabric 1.x.
Moreover invoke documentation epxlicitly shows example how to use invoke to
build sphinx docs. See https://www.pyinvoke.org/

# About

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


```bash
pyenv install
pyenv virtualenv fse
pyenv activate fse

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
