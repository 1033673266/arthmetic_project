class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = nums1 + nums2
        nums.sort()
        n1 = (len(nums)-1)//2
        n2 = len(nums)//2
        return (nums[n1] + nums[n2])/2
