"""
Given a set of N people (numbered 1, 2, ..., N), we would like to split everyone into two groups of any size.

Each person may dislike some other people, and they should not go into the same group.

Formally, if dislikes[i] = [a, b], it means it is not allowed to put the people numbered a and b into the same group.

Return true if and only if it is possible to split everyone into two groups in this way.



Example 1:

Input: N = 4, dislikes = [[1,2],[1,3],[2,4]]
Output: true
Explanation: group1 [1,4], group2 [2,3]
Example 2:

Input: N = 3, dislikes = [[1,2],[1,3],[2,3]]
Output: false
Example 3:

Input: N = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
Output: false


Note:

1 <= N <= 2000
0 <= dislikes.length <= 10000
1 <= dislikes[i][j] <= N
dislikes[i][0] < dislikes[i][1]
There does not exist i != j for which dislikes[i] == dislikes[j].
"""

from collections import defaultdict

class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def add_edge(self, v, w):
        self.graph[v].append(w)
        self.graph[w].append(v)

    def dfs(self, node, color, c):
        if node in color:
            return color[node] == c

        color[node] = c

        for neighbour in self.graph[node]:
            if self.dfs(neighbour, color, -c) is False:
                return False
        return True


class Solution(object):
    def possibleBipartition(self, N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        node_graph = Graph(N)
        color = {}

        for i in range(len(dislikes)):
            node_graph.add_edge(dislikes[i][0], dislikes[i][1])

        for node in node_graph.graph:
            if node not in color:
                if node_graph.dfs(node, color, 1) is False:
                    return False
        return True
