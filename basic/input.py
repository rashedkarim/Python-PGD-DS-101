var = input("Enter two numbers: ").split()

# print(var, type(var))
# print(var[1], type(int(var[1])))
sum = 0
for x in var:
    sum+= int(x)
print("Sum: ", sum)

