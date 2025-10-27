import string
import keyword

name = input()

if not name:
    print(False)
elif name[0].isdigit():
    print(False)
elif any(c.isupper() for c in name):
    print(False)
elif any(c in string.punctuation.replace("_", "") for c in name):
    print(False)
elif name.count("_") > 1:
    print(False)
elif name in keyword.kwlist:
    print(False)
else:
    print(True)
