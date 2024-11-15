head = {
    "id": 1,
    "name": "Rashed"
}

body = [
    ("apple", 2, 200, 400),
    ("Orange", 2, 300, 600),
]
foot = {
    "total": 1000,
    "inword": "One Thousand Taka"
}

invoice = [
    {"header": head},
    {"body": body},
    {"footer": foot},
]

for i in invoice:
    print(i)