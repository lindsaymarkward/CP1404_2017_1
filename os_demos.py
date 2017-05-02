"""OS examples."""

import os
# result = os.system("ls")
# print(result)

# print(os.getcwd())
# print(os.listdir(os.getcwd()))
# os.rename("others.csv", "o.csv")

# for stuff in os.walk(os.getcwd()):
#     print(stuff)

# find all Python files with functions defined in them
for filename in os.listdir('.'):
    # print(filename)
    if filename.endswith('.py'):
        # print(filename)
        with open(filename) as f:
            if "def " in f.read():
                print(filename)

# rename all CSV files to UPPERCASE
for filename in os.listdir('.'):
    if filename.lower().endswith('.csv'):
        os.rename(filename, filename.upper())
