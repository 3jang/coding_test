def solution(s):
    colon = {')': '(', ']': '[', '}': '{'}
    stack = []
    for ch in s:
        if ch == '(' or ch == '[' or ch == '{':
            stack.append(ch)
        else:
            if stack and stack[-1] == colon[ch]:
                stack.pop()
            else:
                return False
    if stack:
        return False
    return True