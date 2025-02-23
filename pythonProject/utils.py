def find_max(numbers):
    max_no = numbers[0]
    for number in numbers:
        if number > max_no:
            max_no = number
    print(max_no)