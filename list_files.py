
input_file = open("subjects.txt")
subjects = input_file.readlines()
input_file.close()

subjects = [subject.strip() for subject in subjects]
print(subjects)

# for subject in subjects:
#     if subject[2] == '1':
#         print(subject)

first_year_subjects = [subject for subject in subjects if subject[2] == '3']
print(first_year_subjects)
