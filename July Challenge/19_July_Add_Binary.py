class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        total_sum = int(a, 2) + int(b, 2)

        return '{:b}'.format(total_sum)
