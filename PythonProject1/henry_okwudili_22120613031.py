# Problem 1: (1)	f(x) =10^x +x-4 , x0  = 0
# Problem 2: (2)	f(x) =10^x  +x-4 , £(0,1)
import math

def f(x):
    eqn = float((10 ** x) + x - 4)
    return eqn


def df(x):
    eqn1 = float(((10 ** x) * math.log(10)) + 1)
    return eqn1


# Implement Newton Raphson Method
def newton():
    x = float(input("Enter initial number: "))
    for i in range(20):
        fx = f(x)
        dfx = df(x)
        x_new = x - f(x) / df(x)
        print(f"Iteration {i + 1}: x = {x:.6f}, f(x) = {fx:.6f}, dfx = {dfx:.6f}")
        x = x_new
    print(f"x = {x:.6f}")


# Implement Bisection Method
def bisection_method():
    a = float(input("Enter a0: "))
    b = float(input("Enter b0: "))

    for i in range(20):
        m = (a + b) / 2
        fm = f(m)
        fa = f(a)
        # fb = f(b)
        print(f"Iteration {i + 1}: m{i} = {m:.6f}, a = {a:.6f}, b = {b:.6f}, m = {m:.6f}, f(m) = {fm:.6f}")

        if fa * fm < 0:
            b = m
        else:
            a = m

    print(f"Final approximation: x = {m:.6f}\n")


print("""
    Which equation would you like to solve?
    Enter 1 for Netwon-Raphson 
    Enter 2 for Bisection Method 
""")
choice = input("> ")
if choice == "1":
    print("Carrying out Newton Raphson's Method for 20 iterations  ...")
    newton()
if choice == "2":
    print("Carrying out Bisection Method for 20 iterations ...")
    bisection_method()
else:
    print("Invalid choice")



