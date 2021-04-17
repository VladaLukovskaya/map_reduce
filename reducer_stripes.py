import sys

(item, stripe) = (None, dict())


# def dict_sum(op1, op2):
#     new_keys = op1.keys()
#     for elem in new_keys:
#         if elem in op2.keys():
#             op2[elem] += op1[elem]
#         else:
#             op2[elem] = op1[elem]
#     result = op2[item]
#     return result


for line in sys.stdin:
    line = line.strip()
    (key, value) = line.strip().split('\t')
    value_dict = eval(value)
    if value != '{}':
        if item and item != key:
            print(f'{item}\t{stripe}')
            stripe = value_dict
        else:
            for element in value_dict:
                if element in stripe:
                    stripe[element] += value_dict[element]
                else:
                    stripe.update({element: value_dict[element]})
        item = key

if item:
    print(f'{item}\t{stripe}')
