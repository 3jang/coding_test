from collections import deque

def solution(prices):
    answer = [0 for _ in range(len(prices))]
    stack = deque()
    for idx, price in enumerate(prices):
        while stack and stack[-1][1] > price:
            idx1, price1 = stack.pop()
            answer[idx1] = idx-idx1
        stack.append((idx, price))

    while stack:
        idx1, price1 = stack.pop()
        answer[idx1] = len(prices) - idx1 -1 
    answer[len(prices)-1] = 0
    
    return answer