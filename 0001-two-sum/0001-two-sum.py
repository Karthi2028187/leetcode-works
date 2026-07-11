class Solution:
    def twoSum(self, nums, target):
        d = {}
        i = 0

        while i < len(nums):
            complement = target - nums[i]

            if complement in d:
                return [d[complement], i]

            d[nums[i]] = i
            i += 1