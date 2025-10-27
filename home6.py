import string

text = input()
words = text.split()

cleaned_words = []
for word in words:
    w = ''.join(c for c in word if c not in string.punctuation)
    if w:
        cleaned_words.append(w.capitalize())

hashtag = '#' + ''.join(cleaned_words)
hashtag = hashtag[:140]

print(hashtag)
