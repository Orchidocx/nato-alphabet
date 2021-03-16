import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_alphabet = {row.letter: row.code for (index, row) in data.iterrows()}

word = input("Enter a word: ").upper()
while word != "0":
    result = [nato_alphabet[letter] for letter in word]
    print(result)
    word = input("Enter a new word (enter 0 to exit): ").upper()

