#coding: utf-8
"""
Count Vowels – Enter a string and the program counts the number of vowels in the text.
For added complexity have it report a sum of each vowel found.
"""
import re


def count_vowels(string):
    """Count the number of vowels in the given string.

    Keyword arguments:
        string -- The string to count the vowels

    Returns:
        A dictionary where the keys are the vowel
    """
    # Create a dictionary with the vowels as keys
    vowels_dict = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0, 'total': 0}

    # Convert the string to lower
    string = string.lower()

    # Extract all the vowels using regular expression and ignoring case
    vowels = re.findall('[aeiou]', string, re.IGNORECASE)

    # Fin each vowel and adds to the dictionary the count
    for vowel in vowels:
        if vowel in vowels_dict:
            vowels_dict[vowel] += 1
            vowels_dict['total'] += 1

    return vowels_dict


if __name__ == '__main__':

    # Prompt to the user for the string
    word_to_check = raw_input("Please, ingress a word o sentence to count the vowels: ")

    vowels = count_vowels(word_to_check)

    print "The total of vowels are %d.\nA: %d\nE: %d\nI: %d\nO: %d\nU: %d\n" % (
        vowels['total'], vowels['a'], vowels['e'], vowels['i'], vowels['o'], vowels['u'],
    )
