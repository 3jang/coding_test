def solution(operations):
    answer = []
    for operation in operations:
        command, num = operation.split()
        num = int(num)
        if command == 'I':
            answer.append(num)
        elif command == 'D' and answer:
            if num == 1:
                answer.remove(max(answer))
            else:
                answer.remove(min(answer))
    if not answer:
        return [0, 0]
    answer.sort()
    return [answer[-1], answer[0]]