#!/usr/bin/env python

import sys

pair, count = None, 0

for line in sys.stdin:
    key, value = line.split('\t')
    if pair and pair != key:
        print(f'{pair}\t{count}')
        pair, count = key, int(value)
    else:
        pair, count = key, count + int(value)

if pair:
    print(f'{pair}\t{count}')
