# Pizza project
This is the final assignment for the base Python course within the Avito Academy of Analysts.

## About
The task is to develop a program with a CLI to simulate pizza delivery. It is required to describe recipes with classes, add several sizes of pizzas, implement a method for comparing pizza classes and the dict() method, which displays a pizza recipe in the form of a dictionary. It is also proposed to write a "log" decorator that takes one parameter - a pattern, and outputs a random number. A decorator can be applied to both a regular function and a class method.

## CLI
To work with the command line interface, the Click library is used. The program can be launched in two modes: order and menu.

1. order mode: the command prepares the pizza, the flag --delivery delivers it by courier.
2. menu mode: displays the menu

## Docstrings
All code must contain docstrings and annotations

## Tests
Some tests must be written.

## PEP8
The code must be written in PEP8 and verified with mypy and flake8 linters. For auto-correction, the black autoformatter is used.

# Install and running
1. For install:
```
    $ git clone git@github.com:yavnolib/aaa-final-task.git
    $ cd aaa-final-task
    $ python3 -m venv venv
    $ source venv/bin/activate
    $ pip install requirements.txt
```

2. Run tests:
```
    $ pytest -v .
```

3. Run programme:
```
    $ python main.py menu
    $ python main.py order --delivery pepperoni
```
