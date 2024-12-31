import heapq

def solution(scovilles, K):
    min_heap_scoville = []
    for scoville in scovilles:
        heapq.heappush(min_heap_scoville, scoville)
    answer = 0
    while min_heap_scoville:
        min_scoville1 = heapq.heappop(min_heap_scoville)
        if min_scoville1 > K:
            return answer
        answer += 1
        if min_heap_scoville:
            min_scoville2 = heapq.heappop(min_heap_scoville)
            heapq.heappush(min_heap_scoville, min_scoville1 + 2 * min_scoville2)    
    return -1