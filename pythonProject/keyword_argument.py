def greet_user(first_name, last_name):
    print(f'Hi there {first_name} {last_name}!')
    print('Welcome aboard')

# positional arguments work with respective positioning of arguments with parameters
# keyword arguments work by sort of instantiating the parameters to the arguments within the called function
# keyword arguments improve readability

print("Start")
greet_user(last_name="smith", first_name="john")
print("Finish")