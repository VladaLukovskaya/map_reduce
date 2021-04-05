import sys

pairs_with_count = dict()
for line in sys.stdin:
    line = line.strip()
    pair, count = line.split('\t')
    if not pairs_with_count.get(pair):
        pairs_with_count[pair] = int(count)
    else:
        pairs_with_count[pair] += int(count)

for pair, count in pairs_with_count.items():
    print(pair, count, sep='\t')
