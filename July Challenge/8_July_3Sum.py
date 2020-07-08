class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.nums = sorted(nums)
        self.result = set()
        for i in range(len(nums)):
            a = self.nums[i]
            b_c = 0 - a
            self.getTwoSome(i+1, len(self.nums)-1, b_c)

        return self.result

    def getTwoSome(self, start, end, x):
        while start < end:
            two_sum = self.nums[start] + self.nums[end]

            if two_sum < x:
                start += 1
            elif two_sum > x:
                end -= 1
            else:
                self.result.add((0-two_sum, self.nums[start], self.nums[end]))
                start += 1
                end -= 1