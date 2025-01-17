def solution(s):
    answer = 0
    n = len(s)

    for i in range(n):
        stack = []
        for j in range(n):
            c = s[(i+j) % n]
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            else:
                if not stack:
                    break
                if c == ')' and stack[-1] == '(':
                    stack.pop()
                elif c == ']' and stack[-1] == '[':
                    stack.pop()
                elif c == '}' and stack[-1] == '{':
                    stack.pop()
                else:
                    break
        else:  # for ~ else 구문: for문이 break에 의해 끝나지 않고 끝까지 수행된 경우 동작하는 구문
            if not stack:
                answer += 1
    return answer

                
