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
    words = text_string.split()
    
    for i in range(len(words)-2):
        bi_gram = (words[i], words[i + 1])

        if bi_gram in chains:
            chains[bi_gram].append(words[i+2])
        else:
            chains[bi_gram] = [words[i+2]]

    last_bi_gram = (words[-2],words[-1])
    if last_bi_gram in chains:
        chains[last_bi_gram].append(None)
    else:
        chains[last_bi_gram] = [None]

    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    current_key = choice(chains.keys())
    text = current_key[0] + " " + current_key[1]

    while True:

        chosen_word = choice(chains[current_key])
        if not chosen_word:
            #equivalent to: if chosen_word is None
            break
        text = text + " " + chosen_word
        current_key = (current_key[1], chosen_word)
        
    return text 

input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# print chains

# Produce random text
random_text = make_text(chains)

print random_text
