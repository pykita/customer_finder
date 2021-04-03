# Customer locater script 

A simple command line tool that outputs customers that are located within the given radius 
from the predifined location in Dublin.

## Installation

1. Make sure you have `Python` installed of version 3.7 or higher.
2. Ensure `pip` package manager is installed.
3. Ensure `make` is also installed.
3. Install virtualenv
    1. On mac run `pip3 install virtualenv`
    2. On ubuntu run `apt-get install python3-venv`
4. Create virtual environment using `python3 -m venv .venv`. This is done to have a clean installation.

## Create a virtual environment

1. To activate the virtual environment run `source .venv/bin/activate`.
2. Install all dependencies by running `pip3 install -r requirements.txt`.

## Running the cli

To run cli execute `python3 -m cli --input-file customers.txt --output-file output.txt --radius 100`. This is also can be done from the makefile by running `make run`

## Running tests

To run tests execute `make tests`.

## Tear down the virtual environment

Execute `deactivate` to exit the virtual environment

