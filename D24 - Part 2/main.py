# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
import os.path

names_path = "/Users/lokeshgupta/Coding 101/100 Days of Python/D24 - Part 2/Input/Names/invited_names.txt"
letter_path = "/Users/lokeshgupta/Coding 101/100 Days of Python/D24 - Part 2/Input/Letters/starting_letter.txt"
save_path = "/Users/lokeshgupta/Coding 101/100 Days of Python/D24 - Part 2/Output/ReadyToSend"

f = open(names_path, "r")
names = f.readlines()
# print(names)

# l = open(letter_path, "r")
# letter = l.readlines()
# print(letter)

with open(letter_path) as file:
    content = file.read()
    # print(content)

for n in range(len(names)):
    names[n] = names[n].strip()
print(names)
print(content)

# testletter = content.replace("[name]",names[0])
# print(testletter)

for n in names:
    completeName = os.path.join(save_path, f"letter_for_{n}.txt")
    file1 = open(completeName, "w")
    toFile = content.replace("[name]", n)
    file1.write(toFile)
    file1.close()
