phone = input("Phone: ")
# digits_mapping = {
#     "1": "one",
#     "2": "two",
#     "3": "three",
#     "4": "four",
# }

# integer to string mapping
# output = ""
# for ch in phone:
#     digits_mapping.get(ch, "!")
#     output += digits_mapping.get(ch, "!")
# print(output)

message = input(">")
words = message.split(' ')
emojis = {
    ":)":"😁",
    ":(":"☹️"
}
output = ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)