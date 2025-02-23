names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
print(names[2:3])
names[0] = 'Jon'
print(names)

numbers = [1, 3, 4, 6, 5]
num = numbers[0]
for i in numbers:
    if i>num:
        num = i
print(f"{num} is the highest number")

numbers2 = [1, 3, 4, 6, 5]
max_no = numbers2[0]
for number in numbers2:
    if number>max_no:
        max_no = number
print(max_no)