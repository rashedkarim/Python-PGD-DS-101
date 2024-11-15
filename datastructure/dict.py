customer = {
    "id": 1,
    "name": "Rashed"
}

print(customer.items())
print(customer.keys())
print(customer.values())
print(customer.get("id", "Not found"))
var = customer.get("name")
print(var, type(var))

for k, v in customer.items():
    print(f"key = {k}, value = {v}")


