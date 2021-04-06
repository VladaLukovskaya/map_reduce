import sys

# pairs_with_count = dict()
# for line in sys.stdin:
#     line = line.strip()
#     pair, count = line.split('\t')
#     if not pairs_with_count.get(pair):
#         pairs_with_count[pair] = int(count)
#     else:
#         pairs_with_count[pair] += int(count)

(pair, count) = (None, 0)

for line in sys.stdin:
    (key, value) = line.split('\t')
    if pair and pair != key:
        print(f'{pair}\t{count}')
        (pair, count) = (key, int(value))
    else:
        (pair, count) = (key, count + int(value))

if pair:
    print(f'{pair}\t{str(count)}')

# for pair, count in :
#     print(pair, count, sep='\t')
