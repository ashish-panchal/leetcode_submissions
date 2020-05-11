"""
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Output: true
Example 2:

Input: 14
Output: false
"""


class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """

        """
        A perfect square always ends with digit: 0, 1, 4, 5, 6, 9
        """

        last_digit = [0, 1, 4, 5, 6, 9]

        if num == 0:
            return False

        if num == 1:
            return True

        if int(str(num)[len(str(num))-1]) not in last_digit:
            return False
        else:
            temp = int(num/2)

            while temp*temp >= num:
                temp = temp/2

            while temp*temp <= num:
                if temp*temp == num:
                    return True
                else:
                    temp += 1

            return False
