import itertools

t1 = (3,4)
t2 = (10,5)

res = [(a, b) for a in t1 for b in t2] + \
      [(a, b) for a in t2 for b in t1]

print(str(res))