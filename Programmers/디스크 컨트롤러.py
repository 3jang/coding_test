import heapq
from collections import deque

def solution(jobs):
    answer = 0
    ready_queue = []
    sorted_jobs = deque(sorted([tup + [idx] for idx, tup in enumerate(jobs)]))
    num_of_tasks = len(jobs)
    time = 0

    while ready_queue or sorted_jobs:
        # Add all jobs that are ready to the priority queue
        while sorted_jobs and sorted_jobs[0][0] <= time:
            submitted_time, running_time, idx = sorted_jobs.popleft()
            # Push into the heap based on running time (shortest job first)
            heapq.heappush(ready_queue, (running_time, submitted_time, idx))
        
        if ready_queue:
            # Process the shortest job in the ready queue
            running_time, submitted_time, idx = heapq.heappop(ready_queue)
            time += running_time
            answer += time - submitted_time
        else:
            # If no jobs are ready, jump time to the next job's submission time
            time = sorted_jobs[0][0]

    return answer // num_of_tasks