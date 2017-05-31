"""Generate markov text from text files."""


from random import choice
from sys import argv


def open_and_read_file():
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    file_paths = argv[1:]
    text = ""

    for file_path in file_paths:
        with open(file_path) as f:
            text += f.read()

    return text


def make_chains(text, n):
    """Takes input text as string; returns dictionary of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
    """

    chains = {}

    words = text.split()

    # 'n' instead of 2 (number of items in tuple)
    for i in range(len(words) - n):
        # sub num by 'n'
        # slice of the list from tuple(list[i : i + n])
        key = tuple(words[i:i + n])

        value = words[i + n]
            # words[i + n]

        if key not in chains:
            chains[key] = []

        chains[key].append(value)

    return chains


def make_text(chains):
    """Returns text from chains."""

    words = []

    while True:

        current_key = choice(chains.keys())
        # random key from chains.keys()
        if current_key[0][0].isupper():
            break

    words.extend(list(current_key))

    while True:

        chosen_word = choice(chains[current_key])
            # random word from chains[current_key]

        new_key = list(current_key[1:]) + [chosen_word]

        new_key = tuple(new_key)
        current_key = new_key

        words.append(current_key[-1])

        if new_key[-1][-1] in ['.', '?', '!']:
            break

    return " ".join(words)


# Open the file and turn it into one long string
input_text = open_and_read_file()

# Get a Markov chain
chains = make_chains(input_text, 3)

# # Produce random text
random_text = make_text(chains)

print random_text
