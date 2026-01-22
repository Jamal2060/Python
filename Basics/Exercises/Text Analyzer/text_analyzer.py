"""
==================================================================================================
1. Input a sentence; output number of characters, words, vowels, consonants, most frequent letter.
==================================================================================================
"""

import string

vowels = 'aeiou'
consonants = 'bcdfghjklmnpqrstvwxyz'
digits = '0123456789'
pun = string.punctuation

sentence = input("Enter a sentence to analyze: ")

# 1. Number of words.
print(f"The number of words in your sentence is: {len(sentence.split())}")

# 2. Number of characters
print(f"The number of characters in your sentence is: {len(sentence)}")

vow = 0
cons = 0
digit = 0
punc = 0
spaces = 0
for char in sentence:
    if char in vowels:
        vow += 1
    elif char in consonants:
        cons += 1
    elif char in digits:
        digit += 1
    elif char in pun:
        punc += 1
    else:
        spaces += 1

# 3. Number of vowels
print(f"Number of vowels: {vow}")

# 4. Number of consonants
print(f"Number of consonants: {cons}")

# 5. Number of digits
print(f"Number of digits: {digit}")

# 6. Number of special characters
print(f"Number of punctuations: {punc}")

# 7. Number of whitespaces
print(f"Number of spaces: {spaces}")

