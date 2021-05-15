from heapq import heappop, heappush
from collections import defaultdict
import sys

# [頂点数, 辺の数, 始点ノード]
size, edge, s = map(int, input().split())
graph = defaultdict(list)
INF = sys.maxsize
for _ in range(edge):
    # 場合によって a -= 1; b -= 1
    a, b, d = map(int, input().split())
    graph[a].append((b, d))
    graph[b].append((a, d))
"""
入力:
4 5 0
0 1 1
0 2 4
1 2 2
2 3 1
1 3 5
出力: 
[0, 1, 3, 4]
"""


def dijkstra(s: int, size: int):
    dist = [INF] * size
    heap = [(s, 0)]
    dist[s] = 0
    seen = [False] * size
    while heap:
        v, d = heappop(heap)
        seen[v] = True
        for next_v, d in graph[v]:
            if seen[next_v]:
                continue
            if dist[next_v] > dist[v] + d:
                dist[next_v] = dist[v] + d
                heappush(heap, (next_v, dist[next_v]))
    return dist


print(dijkstra(s, size))


