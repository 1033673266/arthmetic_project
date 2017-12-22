class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        index = 0
        result = 0
        for i in str(abs(x)):
            result += int(i) * 10 ** index
            index += 1
        if result >= 2 ** 31:
            return 0
        if x != abs(x):
            result *= -1

        return result

if __name__ == '__main__':
    sol = Solution()
    print(sol.reverse(12345))