def solution(arr):
    answer = [arr[i] for i in range(len(arr)) if i == 0 or arr[i] != arr[i-1]]
    return answer