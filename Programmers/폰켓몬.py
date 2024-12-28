def solution(nums):
    answer = 0 # the answer is the number of phoneketmon
    max_num_phoneketmon = len(nums) // 2 # the maximum number of phoneketmon
    phoneketmon = set(nums) # remove duplicates
    if len(phoneketmon) >= max_num_phoneketmon: # if the number of phoneketmon is greater than or equal to the maximum number of phone
        answer = max_num_phoneketmon # the answer is the maximum number of phoneketmon
    else: # if the number of phoneketmon is less than the maximum number of phone
        answer = len(phoneketmon) # the answer is the number of phoneketmon
    return answer