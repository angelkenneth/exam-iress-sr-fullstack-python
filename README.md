# Toy Robot Code Challenge by Iress

🤖

## Setup

### Application Setup

```
$ python3 -V
Python 3.8.19
```

This application has no dependencies, hence, no additional `pip3 install` needed

The lowest Python version that I got this to work was with `3.8`, which comes pre-installed on most modern machines, hence, I hope you will not need `venv`

### Unittest Setup

```
pip3 install "pytest>=4.6.0"
```

`pytest` is the only dev dependency

The lowest version of `pytest` that I got this to run was `4.6.0`, if you already have it installed on you global, it is likely you can run the unit tests already

#### Pipenv Method

If you have [pipenv](https://pipenv.pypa.io/en/latest/installation.html) installed, you only need to run this at the project's root directory:

```
pipenv install
```

## Application Startup

```
python3 ./main.py
```

## Unittest Execution

```
python3 -m pytest
```

Or with [pipenv](https://pipenv.pypa.io/en/latest/installation.html):

```
pipenv run pytest
```

## Demonstrations

### Application

![Iress-App-Demo.gif](/Iress-App-Demo.gif)

### Unitest

![Iress-Unittest-Demo.gif](/Iress-Unittest-Demo.gif)
