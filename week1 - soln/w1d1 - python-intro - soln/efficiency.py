# Updated for Python 3

def list_of_words(f):
    """
    Create a list of all the unique words in the text file given.

    INPUT: file
    OUTPUT: list of words
    """

    words = set()  # Use a set instead of a list if you need to check
                   # membership in it!
    for line in f:
        for word in line.strip().split():
            words.add(word)
    return list(words)


def find_new_words(f, word_dict):
    """
    Given a text file and a dictionary whose keys are words, return a list
    of the words in the file which are not in the dictionary.

    INPUT: file, dictionary
    OUTPUT: list
    """

    words = set()
    for line in f:
        for word in line.strip().split():
            if word not in word_dict:  
                words.add(word)
    return list(words)


def get_average_score(f, word_dict):
    """
    Given a text file and a dictionary whose keys are words and values are a
    score for the word, return the average score of all the words in the
    document. You should assume that missing words have a score of 1.

    INPUT: file, dictionary
    OUTPUT: float
    """

    score = 0
    count = 0
    for line in f:
        for word in line.strip().split():
            # Don't use try excepts if it can be avoided!
            score += word_dict.get(word, 1)
            count += 1
    return float(score) / count


def find_high_valued_words(word_dict, value):
    """
    Return the items from word_dict whose values are larger than value.

    INPUT: dict, float
    OUTPUT: list
    """
    return [key for key, val in word_dict.items() if val > value]
