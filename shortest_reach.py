from collections import defaultdict, deque
import sys
sys.stdin = open("input.txt", "r")

class Graph:
    def __init__(self, n):
        super().__init__()
        self.node_to_edge = defaultdict(set)
        self.num_node = n

    def connect(self, x, y):
        self.node_to_edge[x].add(y)
        self.node_to_edge[y].add(x)
        return 0
    
    def find_all_distances(self, s):
        seen = set()
        queue = deque()
        queue.append((s, 0))
        seen.add(s)
        node_to_cost = {}

        result = []

        while queue:
            node, cost = queue.popleft()
            if node != s:
                node_to_cost[node] = cost

            for neighbor in self.node_to_edge[node]:
                if neighbor not in seen:
                    queue.append((neighbor, cost + 6))
                    seen.add(neighbor)

        for i in range(1, self.num_node + 1):
            if i == s:
                continue
            if i in node_to_cost:
                result.append(node_to_cost[i])
            else:
                result.append(-1)
        print(" ".join(map(str, result)))
        return 0

t = int(input())
for i in range(t):
    n, m = [int(value) for value in input().split()]
    graph = Graph(n)
    for i in range(m):
        x, y = [int(x) for x in input().split()]
        graph.connect(x, y) 
    s = int(input())
    graph.find_all_distances(s)