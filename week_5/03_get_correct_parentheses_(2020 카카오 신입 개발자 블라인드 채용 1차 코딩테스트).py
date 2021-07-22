from collections import deque
balanced_parentheses_string = "()))((()"

def is_correct_parentheses(string): # 올바른 괄호인지 확인
    stack = []
    for s in string:
        if s == '(':
            stack.append(s)
        elif stack: #스택이 존재 할때
            stack.pop()
    return len(stack) == 0

def separate_to_u_v(string): # u, v로 분리
    queue = deque(string)
    left, right = 0, 0
    u, v = "", ""

    while queue: # 큐사용
        char = queue.popleft()
        u += char
        if char == '(':
            left += 1
        else:
            right += 1
        if left == right: # 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 합니다. 즉, 여기서 괄 쌍이 더 생기면 안됩니다.
            break
    
    v = ''.join(list(queue))
    return u, v

def reverse_parentheses(string): # 뒤집기
    reversed_string = ""
    for char in string:
        if char == '(':
            reversed_string += ")"
        else:
            reversed_string += "("
    return reversed_string

#1. 입력이 빈 문자열인 경우, 빈 문자열 반환
def change_to_correct_parentheses(string):
    if string == '': # 1번
        return ''
    # 2번 문자열 w를 두 "균형잡힌 괄호 문자열" u,v로 분리
    # 단,u는 "균형잡힌 괄호 문자열"로 더 이상 분리 할수 없어야함
    # v는 빈 문자열이 될수 있음
    # ( ) 개수가 같아야함
     
    u, v = separate_to_u_v(string) 
    if is_correct_parentheses(u): # 3번
        return u + change_to_correct_parentheses(v)
    else: # 4번
        # 4.1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다.
        # 4.2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다.
        # 4.3. ')'를 다시 붙입니다.
        # 4.4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다.
        # 4.5. 생성된 문자열을 반환합니다.
        return '(' + change_to_correct_parentheses(v) + ')' + reverse_parentheses(u[1:-1])

def get_correct_parentheses(balanced_parentheses_string):
    if is_correct_parentheses(balanced_parentheses_string):
        return balanced_parentheses_string
    else:
        return change_to_correct_parentheses(balanced_parentheses_string)

print(get_correct_parentheses(balanced_parentheses_string)) # "()(())()"가 반환 되어야 합니다!