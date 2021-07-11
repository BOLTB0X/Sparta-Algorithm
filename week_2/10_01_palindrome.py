input = "abcb"

def is_palindrome(string):
    n=len(string)

    for i in range(n):
        if string[i]!=string[n-1]:
            return False
    return True


print(is_palindrome(input))