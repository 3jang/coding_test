def solution(clothes):
    answer = 0
    clothes_dict = {}
    for cloth in clothes:
        clothes_dict[cloth[1]] = clothes_dict.get(cloth[1], 0) + 1 # +1 for the same key
    answer = 1 # for multiplication
    for value in clothes_dict.values():
        answer *= value + 1 # +1 for not wearing
    answer -= 1 # -1 for not wearing anything
    return answer