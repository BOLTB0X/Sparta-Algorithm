s = "(())()"

def is_correct_parenthesis(string):
    check=0
    for s in string:
        if check<0:
            break
        elif s=='(':
            check+=1
        elif s==')':
            check-=1
        
    return True if check==0 else False

print(is_correct_parenthesis(s))  # True 를 반환해야 합니다!
print(is_correct_parenthesis("((((")) #False