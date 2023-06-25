# Timer
Timer tool help people get away from the computer.

## How to set up?
```bash
# Make sure your computer installed python 3 and pip3
pip install timer
```

## How to use?
```bash
# Open a new command line

timer

# Enter number of minutes
```

![Timer img 01](doc%2Fimg01.png)

## How to build?

```bash
# setup env
python -m venv env
source ./env/bin/activate

# Install lib
pip install -r requirements.txt

# Build
python -m build

# Install python tool in the local
pip install .
```