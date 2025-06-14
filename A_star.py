import math, heapq

def a_star(graph, start, goal, heuristic):
    open_set = [(0 + heuristic(start), 0, start)]  # (f = g+h, g, 노드)
    came_from = {}  # 최단 경로 역추적을 위한 이전 노드 기록
    g_score = {start: 0}
    while open_set:
        f, g, current = heapq.heappop(open_set)
        if current == goal:  # 목표 도착
            break
        for neighbor, cost in graph[current].items():
            tentative_g = g + cost
            if tentative_g < g_score.get(neighbor, math.inf):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score = tentative_g + heuristic(neighbor)
                heapq.heappush(open_set, (f_score, tentative_g, neighbor))
    # 필요시 came_from을 통해 경로를 재구성 가능
    return g_score.get(goal, math.inf)
