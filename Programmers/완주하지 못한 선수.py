def solution(participant, completion):
    answer = ''
    participant.sort() # sort() method sorts the list in ascending order
    completion.sort() # sort() method sorts the list in ascending order
    for i in range(len(completion)): # compare the elements of the two lists
        if participant[i] != completion[i]: # if the elements are different
            answer = participant[i] # if the elements are different, the participant is the answer
            break
    if answer == '': # if the answer is not found
        answer = participant[-1] # the last participant is the answer
    return answer