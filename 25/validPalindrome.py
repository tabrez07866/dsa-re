s="A man , a plan ,a canal : Panama"
newStr=""
for c in s:
    if c.isalnum():
        newStr+=c.lower()
if newStr==newStr[::-1]:
    print("palindrome")
else:
    print("not palindrome")    
