from collections import deque

def dfs(node_number, computers, is_visited):
    stack = deque()
    stack.append(node_number)
    is_visited[node_number] = True
    while stack:
        now_node = stack.pop()
        for next_node, can_go in enumerate(computers[now_node]):
            if can_go == 1 and not is_visited[next_node]:  
                is_visited[next_node] = True  
                stack.append(next_node)
    
def solution(n, computers):
    answer = 0
    is_visited = [False] * len(computers)
    for i in range(len(computers)):
        if not is_visited[i]:
            dfs(i, computers, is_visited)
            answer += 1
    return answer