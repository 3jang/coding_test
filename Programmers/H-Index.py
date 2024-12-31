def solution(citations):
    # 내림차순 정렬
    citations.sort(reverse=True)
    
    # H-Index 계산
    for i, citation in enumerate(citations):
        if citation <= i:
            return i
    
    # 모든 논문이 조건을 만족하는 경우
    return len(citations)