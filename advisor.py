import sys
import pyhdfs


def get_a_file():
    fs = pyhdfs.HdfsClient(hosts='localhost:9870', user_name='hadoop')
    lines = list()
    with fs.open('/output/part-00000') as f:
        for line in f:
            lines.append(line.decode("utf-8").strip('\n'))
    return lines


def pairs_advisor(reducer_result):
    advisor_items = list()
    if len(sys.argv) > 1:
        item = sys.argv[2]
        for line in reducer_result:
            pair, count = line.split('\t')
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


def stripes_advisor(reducer_result):
    if len(sys.argv) > 1:
        item = sys.argv[2]
        print(item, "is also often purchased with:")
        for line in reducer_result:
            our_item, other_things = line.strip('\n').split('\t')
            if our_item == item:
                other_things = eval(other_things)
                other_things = dict(sorted(other_things.items(), key=lambda x: (-x[1], x[0])))
            if our_item == item:
                i = 1
                for thing in other_things.items():
                    print(f'{i}.', *thing)
                    i += 1


if sys.argv[1] == 'pairs':
    pairs_advisor(get_a_file())
elif sys.argv[1] == 'stripes':
    stripes_advisor(get_a_file())
