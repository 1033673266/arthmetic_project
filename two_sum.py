class Solution:
    @staticmethod
    def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        my_dict = {}
        for i in range(len(nums)):
            x = nums[i]
            if target - x in my_dict:
                return [my_dict[target-x], i]
            my_dict[x] = i