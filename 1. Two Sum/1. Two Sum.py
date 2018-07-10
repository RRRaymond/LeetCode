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
        m_dict = {}
        for i in range(0, len(nums)):
            other = target - nums[i]
            if other in m_dict:
                return [i, m_dict[other]]
            m_dict[nums[i]] = i
