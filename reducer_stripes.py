import sys
import json

items_and_stripes = dict()


def dict_sum(new_item, new_stripe: dict):
    new_keys = new_stripe.keys()
    if new_item in items_and_stripes.keys():
        stripe = items_and_stripes.get(new_item)
        if stripe:
            for key in new_keys:
                if key in stripe.keys():
                    stripe[key] += new_stripe[key]
                else:
                    stripe[key] = new_stripe[key]
    else:
        items_and_stripes[new_item] = new_stripe


for line in sys.stdin:
    line = line.strip()
    item, stripe = line.split('\t')
    if stripe != '{}':
        dict_sum(item, json.loads(stripe))
    # print(item, stripe)
    # if stripe != "{}":
    #     if items_and_stripes.get(item):
    #         new_stripe = items_and_stripes[item] + ' ' + stripe
    #         new_stripe.split(' ')
    #         new_pair = {item: new_stripe}
    #         items_and_stripes.update(new_pair)
    #     else:
    #         items_and_stripes[item] = stripe

# pp = pprint.PrettyPrinter()
# pp.pprint(items_and_stripes)
for key, value in items_and_stripes.items():
    print(key, json.dumps(value), sep='\t')
