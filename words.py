# For a list of words, print out each word on a separate line, 
# but in all uppercase. How can you change a word to uppercase? 
# Ask Python for help on what you can do with strings!

# Turn that into a function, print_upper_words. Test it out. 
# (Don’t forget to add a docstring to your function!)

def print_upper_words(words):
    """Prints out each word on a separate line, uppercased.
    """

    for word in words:
        print(word.upper())

# Change that function so that it only prints words that 
# start with the letter ‘e’ (either upper or lowercase).

def print_upper_words(words):
    """Prints out each word on a separate line, uppercased - 
        only if the word starts w/ the letter, 'e'.
    """

    for word in words:
        if word.startswith('e') or word.startswith('E'):
            print(word.upper())

# Make your function more general: 
# you should be able to pass in a set of letters, 
# and it only prints words that start with one of those letters.

# For example:
# this should print "HELLO", "HEY", "YO", and "YES"

# print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
#                    must_start_with={"h", "y"})

def print_upper_words(words, start_letters):

    """Prints out each word on a separate line, uppercased -
    only if the word starts w/ a letter from a given set.
    """

    for word in words:
        for letter in start_letters:
            if word.startswith(letter):
                print(word.upper())

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"], start_letters={'h', 'y'})