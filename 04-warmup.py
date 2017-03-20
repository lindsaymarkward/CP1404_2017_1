""" Ask the user for their name
Tell them how many vowels are in their name
"""
# count_vowels = 0
# name = input("Name: ")
# for letter in name:
#     if letter.lower() in 'aeiou':
#         count_vowels += 1
# print("Out of {} letters, {} has {} vowels".format(len(name), name,
#                                                    count_vowels))

# name = input("Name: ")
name = "Bobby McAardvark"

count = 0
for letter in name:
    if letter.lower() in 'aeiou':
        count += 1
# print("Out of {} letters, {} has {} vowels".format(len(name), name, count))

capitals = [c for c in name if c.isupper()]
vowels = [c for c in name if c.lower() in 'aeiou']
new_name = "".join([c for c in name if c.lower() not in 'aeiou'])
print(new_name)
# print(capitals)
# print(vowels)
