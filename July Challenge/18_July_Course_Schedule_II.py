class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        self.marked = [False for i in range(numCourses)]
        self.order = []
        self.adj = [[] for i in range(numCourses)]
        self.is_cyclic = False
        self.color = ["WHITE" for i in range(numCourses)]

        for course in prerequisites:
            self.add_edge(course[1], course[0])

        for i in range(numCourses):
            if not self.marked[i]:
                self.color[i] = "GREY"
                self.dfs(i)

        if self.is_cyclic:
            return []
        return self.order[::-1]

    def add_edge(self, v, w):
        self.adj[v].append(w)

    def dfs(self, v):
        self.marked[v] = True

        for nei in self.adj[v]:
            if self.color[nei] == "GREY":
                self.is_cyclic = True
            if not self.marked[nei]:
                self.color[nei] = "GREY"
                self.dfs(nei)

        self.color[v] = "BLACK"
        self.order.append(v)
