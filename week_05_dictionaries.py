
# phonebook = {}
# print(type(phonebook))

# phonebook["Bill"] = '12345'
# phonebook["Ada"] = '61234'
# phonebook["Ada"] = '00001'
# phonebook["Gary"] += '00001'

# print(phonebook)

people_counts = {"boys": 0, "girls": 0}
#
# print(people_counts)
# print(type(people_counts))

# choice = input("Gender: (g/b), - to stop")
# while choice != '-':
#     if choice == 'b':
#         people_counts["boys"] += 1
#     elif choice == 'g':
#         people_counts["girls"] += 1
#     choice = input("Gender: (g/b), - to stop")

people_counts = {'boys': 2, 'girls': 13}

# print(people_counts)
for gender in people_counts:
    print("{:5} - {:2}".format(gender, people_counts[gender]))

for gender, count in people_counts.items():
    print("{:5} - {:2}".format(gender, count))

