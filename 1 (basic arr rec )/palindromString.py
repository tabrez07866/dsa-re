# def is_palindrome(s):
#     s = s.lower()
#     s = ''.join(filter(str.isalnum, s))
#     return s == s[::-1]

# print(is_palindrome("mom0"))


def is_palindrome(s):
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

s = "mom"
print(is_palindrome(s))  # Output: True    