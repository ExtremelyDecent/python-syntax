def print_upper_words(word_list, must_start_with):
    """ function will take a list of words and print out the words that start with the letter in must_start_with in upper case
    """
    for word in word_list:
        for char in must_start_with:
            if word.startswith(char): print(word.upper())



# this should print "HELLO", "HEY", "YO", and "YES"

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
                   must_start_with={"h", "y"})