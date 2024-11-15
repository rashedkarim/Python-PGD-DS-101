add = lambda a, b: a + b
lst = lambda a, b: [a, b]

print(add(12, 13))
print(lst(12, 34))

for x in lst(1, 4):
    print(x)