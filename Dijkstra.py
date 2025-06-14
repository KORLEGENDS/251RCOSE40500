import math
import heapq

def dijkstra(graph, start):
    dist = {v: math.inf for v in graph}  # 출발점으로부터의 거리
    dist[start] = 0
    pq = [(0, start)]  # 우선순위 큐: (현재까지 거리, 노드)
    while pq:
        current_dist, u = heapq.heappop(pq)
        if current_dist > dist[u]:
            continue  # 이미 더 짧은 경로가 발견된 경우 스킵
        # 인접 노드들의 거리 완화(relaxation)
        for v, weight in graph[u].items():
            alt = current_dist + weight
            if alt < dist[v]:
                dist[v] = alt
                heapq.heappush(pq, (alt, v))
    return dist
