# TODO: Create a letter using starting_letter.txt
# For each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# The letters in the folder "ReadyToSend".

recipients = []

with open("./Input/Names/invited_names.txt", "r") as names:
    names = names.readlines()

for name in names:
    name_strip = name.replace("\n", "")
    recipients.append(name_strip)

with open("./Input/Letters/starting_letter.txt", "r") as letter_template:
    letter_template = letter_template.read()

with open("./Input/Names/invited_names.txt", "r") as names:
    for recipient in recipients:
        new_letter = open(f"./Output/ReadyToSend/{recipient}_letter.txt", "w")
        x = letter_template.replace("[name]", recipient)
        new_letter.write(x)

