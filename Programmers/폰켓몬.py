def solution(nums):
    answer = 0
    max_num_phoneketmon = len(nums) // 2
    phoneketmon = set(nums)
    if len(phoneketmon) >= max_num_phoneketmon:
        answer = max_num_phoneketmon
    else:
        answer = len(phoneketmon)
    return answer