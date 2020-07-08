class Solution(object):
    def prisonAfterNDays(self, cells, N):
        """
        :type cells: List[int]
        :type N: int
        :rtype: List[int]
        """

        """
        Optimized steps as result starts getting repeated after cycle of 14
        """
        N = N % 14

        if not N:
            N = 14

        for j in range(N):
            cells = [0] + [cells[i - 1] ^ cells[i + 1] ^ 1 for i in range(1, 7)] + [0]

        return cells

