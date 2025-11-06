from typing import List
import heapq
from collections import defaultdict

class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        class DSU:
            def __init__(self, n):
                self.parent = list(range(n))
                self.size = [1] * n

            def find(self, x):
                if self.parent[x] != x:
                    self.parent[x] = self.find(self.parent[x])
                return self.parent[x]

            def union(self, a, b):
                ra, rb = self.find(a), self.find(b)
                if ra == rb:
                    return
                if self.size[ra] < self.size[rb]:
                    ra, rb = rb, ra
                self.parent[rb] = ra
                self.size[ra] += self.size[rb]

        dsu = DSU(c)
        for u, v in connections:
            dsu.union(u - 1, v - 1)

        comp_heaps = defaultdict(list)
        for i in range(c):
            root = dsu.find(i)
            heapq.heappush(comp_heaps[root], i + 1)

        online = [True] * c
        res = []

        for t, x in queries:
            x -= 1
            if t == 2:
                online[x] = False
            else:
                if online[x]:
                    res.append(x + 1)
                else:
                    root = dsu.find(x)
                    heap = comp_heaps[root]
                    while heap and not online[heap[0] - 1]:
                        heapq.heappop(heap)
                    if not heap:
                        res.append(-1)
                    else:
                        res.append(heap[0])

        return res