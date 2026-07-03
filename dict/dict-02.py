user1 = {
    "name": "Rinkesh",
    "isMarried": False,
    "age": "Unknown",
    "city": "FBD",
    "state": "HR"
}


user1AdditionInfo = {
    "language":["Hindi","English","Kannda"],
    "mobile":"1234568790"
}
user1.update(user1AdditionInfo)
print(user1)
print(user1AdditionInfo)


print(user1["state"])
print(user1.get("country","No country key value available"))