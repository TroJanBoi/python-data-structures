def palindrome(string):
    string = ''.join(char.lower() for char in string if char.isalnum())

    if len(string) <= 1:
        return True
    
    if string[0] != string[-1]:
        return False
    
    return palindrome(string[1:-1])

print(palindrome("abcba"))
print(palindrome("hello world!"))