"""
@author: raymondchen
@date: 2018/7/10
Description:
"""


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = -1
        length = len(nums)
        for i in range(0,length):
            other = target - nums[i]
            if other in nums:
                left = i
                right = nums.index(target - nums[i])
                if right == left:
                    continue
                break
        return [left, right]
