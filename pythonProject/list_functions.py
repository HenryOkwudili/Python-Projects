numbers = [2,1,4,2,5,6,5,8]

for duplicate in numbers:
    if numbers.count(duplicate) > 1:
        numbers.remove(duplicate)
print(numbers)