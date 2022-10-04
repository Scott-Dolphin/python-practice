import evenIndex as ei

"""
Exercise 3: Print characters from a string that are present at an even index number
Write a program to accept a string from the user and display characters that are present at an even index number.

For example, str = "pynative" so you should display 'p', 'n', 't', 'v'.
"""

example = ei.evenIndex('pynative')
print(f'"pynative" will print as "{example}"')

myWord = input('enter a word\n...')

new = ei.evenIndex(myWord)

print(f'"{myWord}" will print as "{new}"')
