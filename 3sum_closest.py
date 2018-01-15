class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        result = None
        i = 0
        if len(nums) == 3:
            return nums[0] + nums[1] + nums[2]
        while i < len(nums) - 2:
            x = i + 1
            y = len(nums) - 1
            while x < y:
                sum = nums[i] + nums[x] + nums[y]
                diff = sum - target
                if diff == 0:
                    return sum

                elif diff > 0:
                    y -= 1
                else:
                    x += 1

                if result is None:
                    result = [abs(diff), sum]
                else:
                    if result[0] > abs(diff):
                        result = [abs(diff), sum]
            i += 1
        return result[1]

nums = [1,1,1,1]
s = Solution()
s.threeSumClosest(nums ,0)