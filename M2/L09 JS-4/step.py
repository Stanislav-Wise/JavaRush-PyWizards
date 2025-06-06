person = {
    "name": "Bob",
    "age": 28,
    "city": "Moscow",
    "isAdmin": True,
    "address": {
        "street": "Ленина",
        "number": 9,
    }
}

print(person.get("name111"))

person["job"] = "Программист"
print(person)

del person["age"]
print(person)


print("name" in person)
print("name12" in person)