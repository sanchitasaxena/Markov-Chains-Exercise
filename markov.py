from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    contents = open(file_path).read()
    # your code goes here

    return contents


def make_chains(text_string):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """

    chains = {}
    #create an empty dictionary
    words = text_string.split()
    #make text into string and then splitting it
    
    for i in range(len(words)-2):
    #for every word in string except for last two words
        bi_gram = (words[i], words[i + 1])
        #created key variable into tuple using two adjacent words
        if bi_gram in chains:
        # if the key is in the dictionary add the next word into list of values/words
            chains[bi_gram].append(words[i+2])
        else:
        # if word is not already in dictionary, create the list where word is placed
            chains[bi_gram] = [words[i+2]]
    #defining variable for last key/tuple 
    last_bi_gram = (words[-2],words[-1])
    #if it is the last bi_gram in dictionary, add None as a value in list of words else add none/ nothing
    if last_bi_gram in chains:
        chains[last_bi_gram].append(None)
    else:
        chains[last_bi_gram] = [None]

    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    #current key is equal to a random key in the dictionary
    current_key = choice(chains.keys())
    #text is a string equal to the first index of the tuple and the second index of the tuple
    text = current_key[0] + " " + current_key[1]
    #create a loop that will repeat until the function reaches the last bi-gram
    while True:
        #created a variable for a random value of the current key
        chosen_word = choice(chains[current_key])
        #equivalent to: if chosen_word is None
        if not chosen_word:
            break
        # if it's not the last key add the chosen_word to the text to string
        text = text + " " + chosen_word
        # select new key
        current_key = (current_key[1], chosen_word)
        
    return text 
# running our text file 
input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# print chains

# Produce random text
random_text = make_text(chains)

print random_text
