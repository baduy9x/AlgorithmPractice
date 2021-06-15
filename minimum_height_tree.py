from collections import defaultdict

class Solution:
    def findMinHeightTrees(self, n, edges):
        path = {}
        adj_list = defaultdict(list)
        for i in range(n - 1):
            path[(edges[i][0], edges[i][1])] = 1
            path[(edges[i][1], edges[i][0])] = 1
            adj_list[edges[i][0]].append(edges[i][1])
            adj_list[edges[i][1]].append(edges[i][0])
        
        
