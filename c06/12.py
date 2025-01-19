def solution(prices):
    N = len(prices)
    times = [0] * N
    stack = [0]

    for i in range(1, N):
        while stack and prices[i] < prices[stack[-1]]:
            j = stack.pop()
            times[j] = i-j
        stack.append(i)
    
    while stack:
        j = stack.pop()
        times[j] = N - 1 - j
            
    return times
