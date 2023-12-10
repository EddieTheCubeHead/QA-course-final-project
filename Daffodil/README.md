## Prerequisites

- python3
- daffodil 3.6.0

Daffodil executable has to be placed under the `daffodil-src/bin/` folder and necessary schema files under the `schemas/` folder.

## Installing requirements

To install requirements please navigate under the Daffodil folder in your command line.

Generate a virtual environment:

    python -m venv venv

Install requirements:

    venv\Scripts\pip install -r requirements.txt

## Running tests

To run the tests, enter the virtual environment (PowerShell):

    venv\Scripts\Activate.ps1

Then just run pytest:

    pytest
