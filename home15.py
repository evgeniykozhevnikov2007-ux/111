import string

def is_palindrome(text):
    allowed = set(string.ascii_letters + string.digits)
    filtered = [c.lower() for c in text if c in allowed]
    return filtered == filtered[::-1]

assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")
