"""
Exercise 4: Remove first n characters from a string
Write a program to remove characters from a string starting from zero up to n and return a new string.

For example:

remove_chars("pynative", 4) so output must be tive. Here we need to remove first four characters from a string.
remove_chars("pynative", 2) so output must be native. Here we need to remove first two characters from a string.
Note: n must be less than the length of the string.
"""

def remove_chars(word:str, index:int):
    if index >= len(word):
        print('index must be less than word.')
        exit()
    return word[index:]

example = 'pynative'

print(f'"{example}, 4" will return {remove_chars(example, 4)}')
print(f'"{example}, 2" will return {remove_chars(example, 2)}')