class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        hash_map = {}

        for i in range(len(nums)):
            if str(nums[i]) not in hash_map:
                hash_map[str(nums[i])] = 1
            else:
                hash_map[str(nums[i])] = hash_map[str(nums[i])] + 1

        sort_nums = sorted(hash_map.items(), key=lambda x: x[1], reverse=True)
        # print sort_nums

        result = []

        for item in sort_nums:
            if k > 0:
                result.append(item[0])
                k -= 1
            else:
                break
        return result