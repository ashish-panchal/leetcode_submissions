class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    self.countPerimeter(i + 1, j, grid)
                    self.countPerimeter(i - 1, j, grid)
                    self.countPerimeter(i, j + 1, grid)
                    self.countPerimeter(i, j - 1, grid)

        return self.count

    def countPerimeter(self, i, j, grid):
        if i < len(grid) and j < len(grid[0]) and i >= 0 and j >= 0:
            if grid[i][j] == 0:
                # print (i,j)
                self.count += 1
        else:
            self.count += 1
