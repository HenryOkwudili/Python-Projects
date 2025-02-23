# For nested loops the inner loop is exhausted first before returning to the outer loop
# In the following nested loop. The iteration for both loops starts from 0
# the second loop finishes its range before the range continues for the outer loops


for x in range(4):
    for y in range(3):
        print(f'({x}, {y})')