
def sortKey(e):
    return len(e)

f = ["green apple", "cherry", "kiwi", "mango", "banana", "1"]
print(f)

obj = dir(f)
for m in obj:
    if("__" not in m):
        print(m)

f.append("olive")
print(f)
print(f.count("apple"))
# tpl = (1,2,3)
# f.extend(tpl)
f.reverse()
f.sort(key=sortKey)
print(f)