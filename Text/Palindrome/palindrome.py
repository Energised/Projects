#coding: utf-8
"""
Check if Palindrome – Checks if the string entered by the user is a palindrome.
That is that it reads the same forwards as backwards like “racecar”
"""


def is_palindrome(string):
    """Check if the string is a palindrome.

    Keyword arguments:
    string -- The string to check if is palindrome

    Returns:
        A boolean
    """
    # Remove all blank spaces
    word = ''.join(string.split())

    # Invert the string using slice syntax.
    reversed_string = word[::-1]

    # Check if the string and the reversed string are equals
    if word == reversed_string:
        return True

    return False


if __name__ == '__main__':

    # Prompt to the user for the string
    word_to_check = raw_input("Please, ingress a word to check if is palindrome: ")

    if is_palindrome(word_to_check):
        print "The word '%s' is palindrome" % (word_to_check,)
    else:
        print "The word '%s' is not a palindrome" % (word_to_check,)