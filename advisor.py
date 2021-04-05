import json
import sys


def pairs_advisor():
    advisor_items = list()
    if len(sys.argv) > 1:
        item = sys.argv[2]
        for line in sys.stdin:
            pair, count = line.strip('\n').split('\t')
            pair = set(pair.split(' '))
            if item in pair:
                advisor_items.append((pair, count))

        advisor_items = sorted(advisor_items, key=lambda x: x[1], reverse=True)
        print(item, "is also often purchased with:")
        i = 1
        for pair, count in advisor_items:
            pair.remove(item)
            print(f'{i}. {pair.pop()} - ({count})')
            i += 1


def stripes_advisor():
    if len(sys.argv) > 1:
        item = sys.argv[2]
        print(item, "is also often purchased with:")
        for line in sys.stdin:
            our_item, other_things = line.strip('\n').split('\t')
            other_things = dict(sorted(json.loads(other_things).items(), key=lambda x: x[1], reverse=True))
            if our_item == item:
                i = 1
                for thing in other_things.items():
                    print(f'{i}.', *thing)
                    i += 1


if sys.argv[1] == 'pairs':
    pairs_advisor()
elif sys.argv[1] == 'stripes':
    stripes_advisor()
