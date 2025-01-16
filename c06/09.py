'''
문제 09 10진수를 2진수로 변환하기

난이도: ⭐️
저자 권장 시간: 30분
권장 시간 복잡도: O(logN)
출제: 저자 출제
날짜: 2025-01-16

제약조건:
    - 없음
'''

#내 풀이
def solution(num):
    stack = []

    while (num > 0):
        stack.append(str(num % 2))
        num  = num // 2
    stack.reverse()
    return ''.join(stack)

#저자 풀이, 스택 활용을 보여주기 위해 `pop()`을 했음. 이로 인해 시간 복잡도가 (logN)^2이 됨.
def solution(decimal):
    stack = []
    while decimal > 0:
        remainder = decimal % 2
        stack.append(str(remainder))
        decimal //= 2

    binary = ""
    while stack:
        binary += stack.pop()

    return binary

# TEST 코드 입니다. 주석을 풀고 실행시켜보세요
#print(solution(10)) #반환값 :  1010
# print(solution(27)) #반환값 :  11011
# print(solution(12345)) #반환값 : 11000000111001
