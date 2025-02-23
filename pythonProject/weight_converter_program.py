weight = int(input("Enter your weight number: "))

scale = input("(L)bs or (K)g: ")

if scale.upper() == "L":
    weight *= 0.453592
    print(f"Your weight is {weight} kg")
elif scale.upper() == "K":
    weight /= 0.453592
    print(f"Your weight is {weight} pounds")


