def reptile(animal):
    return animal == "Crocodile"
def amphibian(animal):
    return animal in ("Frog", "Newt", "Crocodile")

print(reptile("Crocodile"))
print(amphibian("Crocodile"))