def solution(numbers):
    numbers = list(map(str, numbers)) # numbers의 원소를 문자열로 변환
    numbers.sort(key=lambda x: x*3, reverse=True) # numbers의 원소를 3번 반복한 문자열을 기준으로 내림차순 정렬
    answer = str(int(''.join(numbers))) # numbers의 원소를 문자열로 합친 후 정수로 변환하여 다시 문자열로 변환
    return answer 