def solution(s):
    answer = -1
    n = len(s)
    stack = []
    for i in range(n):
        if stack and s[i] == stack[-1]:
            stack.pop()
        else:
            stack.append(s[i])
    
    if not stack:
        answer = 1
    else:
        answer = 0
    
    return answer
