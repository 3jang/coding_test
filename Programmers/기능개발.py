from itertools import groupby, accumulate

def solution(progresses, speeds):
    require_date = list((100 - progress + speed - 1) // speed for progress, speed in zip(progresses, speeds))
    return list(len(list(group)) for _, group in groupby(accumulate(require_date, max)))
