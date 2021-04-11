#!/usr/bin/env python3

import sys

for line in sys.stdin:
    line = line.strip()
    words = line.split()
    words = sorted(words)
    for word_i in words[:]:
        for word_j in words[words.index(word_i)+1:]:
            print(f'{word_i} {word_j}\t1')
