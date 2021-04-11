import sys
# import json

# items_and_stripes = dict()

(item, stripe) = (None, dict())


def dict_sum(new_stripe):
    items_and_stripes = dict()
    new_keys = new_stripe.keys()
    for elem in new_keys:
        if elem in stripe.keys():
            stripe[elem] += new_stripe[elem]
        else:
            stripe[elem] = new_stripe[elem]
    return stripe[elem]


for line in sys.stdin:
    line = line.strip()
    (key, value) = line.strip().split('\t')
    value_dict = eval(value)
    # print('new', key, value)
    if value != '{}':
        if item and item != key:
            # print(f'{item}\t{str(dict_sum(stripe))}')
            print(f'{item}\t{stripe}')
            stripe = value_dict
        else:
            for elem in value_dict:
                # print(elem)
                if elem in stripe:
                    stripe[elem] += value_dict[elem]
                else:
                    stripe.update({elem: value_dict[elem]})
                # print(stripe)
        item = key

if item:
    # print(f'{item}\t{str(dict_sum(stripe))}')
    print(f'{item}\t{stripe}')


