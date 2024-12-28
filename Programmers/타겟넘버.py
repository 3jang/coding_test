def solution(numbers, target):
    answer = 0
    def dfs(idx, result):
        if idx == len(numbers):
            if result == target:
                nonlocal answer
                answer += 1
            return
        dfs(idx + 1, result + numbers[idx])
        dfs(idx + 1, result - numbers[idx])
    return answer