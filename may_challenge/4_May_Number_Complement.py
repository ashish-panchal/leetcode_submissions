"""
Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.



Example 1:

Input: 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.


Example 2:

Input: 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.


Note:

The given integer is guaranteed to fit within the range of a 32-bit signed integer.
You could assume no leading zero bit in the integer’s binary representation.
This question is the same as 1009: https://leetcode.com/problems/complement-of-base-10-integer/
"""


class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        binary_rep = ""
        result = 0

        if num == 0:
            return 1

        while int(num) != 0:
            div = int(num/2)
            rem = num%2

            binary_rep += str(rem)
            num = div

        binary_rep = binary_rep[::-1]

        for i in range(1, len(binary_rep)+1):
            if int(binary_rep[i-1]) != 1:
                result += pow(2,(len(binary_rep)-i)) * 1

        return result