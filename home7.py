import string

s = input()  # например "a-c"
start, end = s.split('-')

letters = string.ascii_letters
print(letters[letters.index(start):letters.index(end)+1])
