
print(True, "type:", type(True))
print(None, "type:", type(None))
print(5, "type:", type(5))
print(5.2, "type:", type(5.2))
print(5+2j, "type:", type(5+2j))
print("Rashed", "type:", type("Rashed"))
print([1,2,3], "type:", type([1,2,3]))
print((1,2,3), "type:", type((1,2,3)))
print({1,2,3}, "type:", type({1,2,3}))
print({"Item":1,"Quantity":2,"Price":30}, "type:", type({"Item":1,"Quantity":2,"Price":30}))
print(bin(65), "type:", type(bin(7)))
print(oct(65), "type:", type(oct(7)))
print(hex(65), "type:", type(hex(7)))
x = 1
print(id(x))
print(hex(id(x)))
x = x + 2
print(id(x))
print(hex(id(x)))


