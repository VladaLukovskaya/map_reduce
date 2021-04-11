import sys
import json
for line in sys.stdin:
    line = line.strip()
    words = line.split()
    words = sorted(words)
    for word_i in words:
        pairs_and_counts = dict()
        left_words = words[:]
        left_words.remove(word_i)
        for word_j in left_words:
            if pairs_and_counts.get(word_j):
                pairs_and_counts[word_j] += 1
            else:
                pairs_and_counts.update({word_j: 1})
        print(word_i, json.dumps(pairs_and_counts), sep='\t')
