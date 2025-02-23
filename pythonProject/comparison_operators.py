temperature = 30

# comparison operators : ==, >, <, !=, etc

if temperature > 30:
    print("It's a hot day")
else:
    print("It's not a hot day")


name = input("Type in your name: ")
if len(name) < 3:
    print("Name must be at least 3 characters")
    name = input("Type in your name: ")

elif len(name) > 50:
    print("Name must be at most 50 characters")
    name = input("Type in your name: ")
else:
    print("Name looks good")
