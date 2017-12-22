class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        result = 0
        for i in range(length):
            char_list = s[i]
            for j in range(i + 1, length):
                if s[j] in char_list:
                    break
                char_list += s[j]

            if len(char_list) > result:
                result = len(char_list)
        return result


if __name__ == '__main__':
    s = 'abcdafhjkla'
    sol = Solution()
    print sol.lengthOfLongestSubstring(s)
