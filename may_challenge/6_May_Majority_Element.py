"""
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
"""

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash_map = {}
        result = {"max": 0, "element": None}
        for i in range(len(nums)):
            if str(nums[i]) not in hash_map:
                hash_map[str(nums[i])] = 1
            else:
                hash_map[str(nums[i])] += 1

        for number in hash_map:
            if hash_map[number] > result["max"]:
                result["max"] = hash_map[number]
                result["element"] = number

        return result["element"]

# Constant Memory approach
"""
int currentWinner, count = 0
for num in nums:
	// empty battlefield
	if count == 0 
		// the currently visible person is winning
		currentWinner = num
		count++
	else
		// the battle is already on
		// opposing force
		if num != currentWinner
			count--
		// reinforcements
		else
			count++
// last side standing
return currentWinner
"""