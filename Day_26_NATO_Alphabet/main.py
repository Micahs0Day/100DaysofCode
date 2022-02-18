import pandas

# Converts CVS file to Dataframe
df = pandas.read_csv("nato_phonetic_alphabet.csv")

# TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

# List Comprehension (Loop over Dataframe and creates Dictionary containing letter:code pair)
nato_dict = {row.letter:row.code for (index, row) in df.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

# Prompts user to enter a word to be converted to Nato.
user_input = input("Enter a word: ")
user_input = user_input.upper()

# Gets every letter in user supplied string, coverts to upper, appends matching dictionary entry to list.
nato_list = [nato_dict[letter] for letter in user_input]

# Prints out the converted NATO list to screen.
print(nato_list)

