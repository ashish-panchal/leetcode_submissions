class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = [1] * n
        num2, num3, num5 = 0, 0, 0

        for i in range(1, n):
            memo[i] = min(2 * memo[num2], 3 * memo[num3], 5 * memo[num5])
            if memo[i] == 2 * memo[num2]:
                num2 += 1
            if memo[i] == 3 * memo[num3]:
                num3 += 1
            if memo[i] == 5 * memo[num5]:
                num5 += 1
        return memo[n - 1]