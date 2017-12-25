class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        negative_list = []
        zero_list = []
        positive_list = []
        result = []
        for i in nums:
            if i < 0:
                negative_list.append(i)
            if i == 0:
                zero_list.append(i)
            if i > 0:
                positive_list.append(i)

        for i in range(len(negative_list)):
            for j in range(i + 1, len(negative_list)):
                another = 0 - (negative_list[i] + negative_list[j])
                if another in positive_list:
                    tmp = sorted([negative_list[i], negative_list[j], another])
                    if tmp not in result:
                        result.append(tmp)

        for i in range(len(positive_list)):
            for j in range(i + 1, len(positive_list)):
                another = 0 - (positive_list[i] + positive_list[j])
                if another in negative_list:
                    tmp = sorted([positive_list[i], positive_list[j], another])
                    if tmp not in result:
                        result.append(tmp)
        if zero_list:
            for i in range(len(positive_list)):
                another = 0 - positive_list[i]
                if another in negative_list:
                    tmp = sorted([positive_list[i], 0, another])
                    if tmp not in result:
                        result.append(tmp)
        if len(zero_list) >= 3:
            result.append([0, 0, 0])

        return result


if __name__ == '__main__':
    sol = Solution()
    a = [-1, 0, 1, 2, -1, -4]
    print sol.threeSum(a)
