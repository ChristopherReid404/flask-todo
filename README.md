# Flask Todo

[![CircleCI](https://img.shields.io/circleci/build/github/ChristopherReid404/flask-todo/master.svg)](https://circleci.com/gh/ChristopherReid404/flask-todo/tree/master)
[![Coverage Status](https://coveralls.io/repos/github/ChristopherReid404/flask-todo/badge.svg?branch=coveralls)](https://coveralls.io/github/ChristopherReid404/flask-todo?branch=coveralls)
[![Last Commit](https://img.shields.io/github/last-commit/ChristopherReid404/flask-todo/master.svg)](https://img.shields.io/github/last-commit/ChristopherReid404/flask-todo/master.svg)
[![License](https://img.shields.io/github/license/ChristopherReid404/flask-todo.svg)](https://img.shields.io/github/license/ChristopherReid404/flask-todo.svg)

This project was started from a tutorial found [Here](https://www.youtube.com/watch?v=Z1RJmh_OqeA&t=1811s) by Jake Rieger.

Simple Todo tracker where you can add/edit/delete tasks.

## Upgrades

- CircleCi Testing, only single test

## Prerequisites

- Python 2.7 or 3.6+
- pipenv

## Installing

```bash
pipenv install
```

## Running

```bash
pipenv run python app.py
```

## Testing

```bash
pipenv run pytest
  or
pipenv run coverage run --source=. -m pytest
pipenv run coverage report
```
