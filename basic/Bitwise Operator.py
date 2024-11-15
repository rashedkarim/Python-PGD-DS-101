x = 7
y = 2

xb = bin(x)
print(x, " = ", xb)

yb = bin(y)
print(y, " = ", yb)

xy = x & y
xyB = bin(xy)
print(f"{x} AND {y} = {xy} {xyB}")

xy = x | y
xyB = bin(xy)
print(f"{x} OR {y} = {xy} {xyB}")

xy = x ^ y
xyB = bin(xy)
print(f"{x} XOR {y} = {xy} {xyB}")

xy = ~ x
xyB = bin(xy)
print(f"~{x} = {xyB} : {xy}")

xy = x << y
xyB = bin(xy)
print(f"{x}<<{y} ({xb}, {yb}) = {xyB} : {xy}")

xy = x >> y
xyB = bin(xy)
print(f"{x}>>{y} ({xb}, {yb}) = {xyB} : {xy}")
