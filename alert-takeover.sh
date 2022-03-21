#!/bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 &&pwd)"
python3 $DIR/takeover.py -l $DIR/targets.txt -t 50