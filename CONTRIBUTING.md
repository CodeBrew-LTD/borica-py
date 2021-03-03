### Publishing a new version of this package

This will only work for collaborators in the PyPI package.
https://pypi.org/project/borica-py/

#### Prerequisites
```
python3 -m pip install --upgrade build twine
```

#### Building and upload
```
python3 -m build
python3 -m twine upload dist/*
# You will be prompted for you pypi credentials
```