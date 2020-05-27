"""
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
Example 2:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
Note: The length of the given binary array will not exceed 50,000.
"""


class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash_map = {}

        hash_map["0"] = 1

        maxlen = 0
        ct = 0

        for i in range(len(nums)):
            num = 0

            if nums[i] == 0:
                num = -1
            else:
                num = 1

            ct += num

            if str(ct) in hash_map:
                maxlen = max(maxlen, i - hash_map[str(ct)])
            else:
                hash_map[str(ct)] = i

        return maxlen
