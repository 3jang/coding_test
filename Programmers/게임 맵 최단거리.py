from collections import deque

def bfs(maps):
    dxdy = [(1,0), (-1,0), (0,1), (0,-1)]
    queue = deque()
    queue.append((0,0,1))
    maps[0][0] = 0
    while queue:
        now_x, now_y, now_cost = queue.popleft()
        if now_x == len(maps[0])-1 and now_y == len(maps)-1:
            return now_cost
        for dx, dy in dxdy:
            next_x = now_x + dx
            next_y = now_y + dy
            if next_x < 0 or next_x >= len(maps[0]) or next_y < 0 or next_y >= len(maps) or maps[next_y][next_x] == 0:
                continue
            maps[next_y][next_x] = 0
            queue.append((next_x, next_y, now_cost+1))

    return -1

def solution(maps):
    return bfs(maps)