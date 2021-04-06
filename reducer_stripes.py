import sys
# import json

# items_and_stripes = dict()

(item, stripe) = (None, dict())


def dict_sum(new_stripe):

    # stripe_sum = sum(new_stripe.values())
    # for internal_key, internal_value in new_stripe.items():
    #     stripe_sum += internal_value
    #     print(stripe_sum)
    #     return {internal_key: internal_key}
    #
    items_and_stripes = dict()
    new_keys = new_stripe.keys()
    print('new_stripe', new_keys)
    for elem in new_keys:
        if elem in stripe.keys():
            stripe[elem] += new_stripe[elem]
        else:
            stripe[elem] = new_stripe[elem]
    print()


for line in sys.stdin:
    line = line.strip()
    (key, value) = line.strip().split('\t')
    value_dict = eval(value)
    print('new', key, value)
    if value != '{}':
        if item and item != key:
            print(f'{item}\t{str(dict_sum(stripe))}')
            stripe = value_dict
        else:
            for k in stripe.keys():
                stripe[k] += value_dict[k]
        item = key
    #
    #     dict_sum(item, json.loads(stripe))

if item:
    print(f'{item}\t{str(dict_sum(stripe))}')


# for key, value in items_and_stripes.items():
#     print(key, json.dumps(value), sep='\t')
