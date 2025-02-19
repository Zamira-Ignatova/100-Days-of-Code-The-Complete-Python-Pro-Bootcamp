import pandas

alphabet_df = pandas.read_csv("phonetic_alphabet.csv")
alph_dictionary = {row.letter: row.code for (index, row) in alphabet_df.iterrows()}
# Create a list of the phonetic code words from a word that the user inputs.
def phonetic_alphabet_generator():
    word = input("Enter a word: ").upper()
    try:
        phonetic_code = [alph_dictionary[letter] for letter in word]
    except KeyError:
        print("Only letters are allowed. Please try again")
        phonetic_alphabet_generator()
    else:
        print(phonetic_code)

phonetic_alphabet_generator()
