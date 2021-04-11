import requests
import sys


def get_a_file():
    hdfs_path = sys.argv[3]
    url = f'http://localhost:9870/webhdfs/v1{hdfs_path}'
    params = {
        'user.name': 'hadoop',
        'op': 'OPEN',
    }
    get = requests.get(url, params=params)
    result = get.text.split("\n")[:-1]
    return result


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


# get_a_file()

if sys.argv[1] == 'pairs':
    pairs_advisor(get_a_file())
elif sys.argv[1] == 'stripes':
    stripes_advisor(get_a_file())
