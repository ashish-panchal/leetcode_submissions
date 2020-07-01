class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        """
        We need to find k such that 1 + 2 + .... + k <= n

        since k(k+1)//2 <= n

        we can use binary search with this condition
        """

        left, right = 0, n

        while left <= right:
            mid = (left + right) // 2

            coins_so_far = mid * (mid + 1) // 2

            if coins_so_far < n:
                left = mid + 1
            elif coins_so_far > n:
                right = mid - 1
            else:
                return mid

        return right