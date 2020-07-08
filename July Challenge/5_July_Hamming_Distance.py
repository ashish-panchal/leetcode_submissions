import math


class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        n = x ^ y
        setBits = 0

        while (n > 0):
            setBits += n & 1
            n >>= 1

        return setBits

