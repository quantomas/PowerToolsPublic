
# https://stackoverflow.com/questions/32544835/python-create-dictionary-using-dict-with-integer-keys
# https://stackoverflow.com/questions/1024847/how-can-i-add-new-keys-to-a-dictionary

data = {'a': 1, 'b': 2, 'c': 3}

data = dict(a=1, b=2, c=3)

data = {k: v for k, v in (('a', 1), ('b',2), ('c',3))}


data = {k: v for k, v in ((5, 1), (3, 2), (4, 3))}
data = {k: v for k, v in ((5, 1.2), (3, 2.0), (4, 3.5))}


for el in data:
    el


# Dict of Lists

d = dict()
d['a'] = [1,2]
d['b'] = [1,2,5,4]
d['c'] = [4,6,45]
d['tl'] = [(5, 1.2), (3, 2.0), (4, 3.5), (1, 2.5), (2, 3.3)]

d['a'].append(4)
d['tl'].append((10, 2.5))


for k, v in d.items():
    print(k)
    print(v)


##
d = {"key1": 10, "key2": 23}

if "key1" in d:
    print("this will execute")


if not ("aa" in d):
    print("key does not exist")
    d["aa"] = []



# https://pyformat.info/
for k, v in data.items():
    print(k)
    print(v)
    print("{} : {}".format(k, v) )


#
# l = [(5, 1.2), (3, 2.0), (4, 3.5)]

l = [(5, 1.2), (3, 2.0), (4, 3.5), (1, 2.5), (2, 3.3)]
len(l)
type(l)
type(l[0])


l_prod = 0.0

for el in l:
    # print(el)
    print("{} : {}".format(el[0], el[1]) )
    l_prod += el[0] * el[1]


l_prod


# https://stackoverflow.com/questions/3121979/how-to-sort-a-list-tuple-of-lists-tuples-by-the-element-at-a-given-index
from operator import itemgetter

l.sort(key=itemgetter(1))


# https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
l_sorted = sorted(l, key = itemgetter(1), reverse = True)
l_sorted




##
# https://stackoverflow.com/questions/16730339/python-add-item-to-the-tuple/16730367

tl = (('a', 1), ('b',2), ('c',3))
tl = tl + (('d', 4))



a = ('2',)
b = 'b'

l = list(a)
l.append(b)

tuple(l)

