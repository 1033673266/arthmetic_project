class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums.sort()
        resultList = []
        i = 0
        while i < len(nums) - 2:
            j = i + 1
            k = len(nums) - 1
            while j < k:
                sums = nums[i] + nums[j] + nums[k]
                if sums == 0:
                    result = sorted([nums[i], nums[j], nums[k]])
                    resultList.append(result)

                    j += 1
                    k -= 1
                    while j < k:
                        if nums[j] != nums[j - 1]:
                            break
                        if nums[k] != nums[k + 1]:
                            break
                        j += 1
                        k -= 1

                elif sums < 0:
                    j += 1
                else:
                    k -= 1
            while i < len(nums) - 2:

                i += 1
                if nums[i] != nums[i - 1]:
                    break
        return resultList


if __name__ == '__main__':
    sol = Solution()
    a = [0, 0, 0]
    print sol.threeSum(a)
