#!/bin/bash

pylint --output-format=json --reports=y cipher.py > pylint_report.json

if [ $? -eq 0 ]; then
    echo "Pylint report:"
    cat pylint_report.json | jq '.[] | {message: .message, score: .score}'

    python3 -m unittest test_decode.py
else
    echo "Error: Pylint failed."
fi