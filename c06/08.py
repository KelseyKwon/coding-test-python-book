'''
문제 08 괄호 짝 맞추기

난이도: ⭐️⭐️
저자 권장 시간: 30분
권장 시간 복잡도: O(N)
출제: 저자 출제
날짜: 2025-01-16

제약조건:
    - 열린 괄호는 자신과 가장 가까운 닫힌 괄호를 만나면 상쇄됩니다.
    - 상쇄 조건은 열린 괄호가 먼저 와야 하고, 열린 괄호와 닫힌 괄호 사이에 아무것도 없어야 합니다.
    - 더 상쇄할 괄호가 없을 때까지 상쇄를 반복합니다.
'''

# 내 풀이
# if not stack과 같은 조건문을 달아야 함. (틀림)
stack = []

def solution(str):
    for i in range((len(str))):
        if str[i] == '(':
            stack.append(str[i])
        elif str[i] == ')':
            stack.pop()
    if (len(stack) == 0):
        return True
    else:
        return False

# 저자 풀이
# 시간 복잡도 O(N)
def solution(s):
    stack = []
    for c in s:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if not stack:
                return False
            else:
                stack.pop()
    if stack:
        return False
    else:
        return True


#print(solution('(())()')) # 반환값 : True
#print(solution('((())()')) # 반환값 : False
