#!/bin/bash

pdoc --html niteru -o docs --force
mv docs/niteru/*.html docs/
rm -r docs/niteru