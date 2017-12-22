class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        x = y = 0
        if numRows == 1:
            return s
        down = True
        str_list = [[] for i in range(numRows)]
        for i in s:

            str_list[x].append(i)
            if x == numRows - 1:
                down = False
            elif x == 0:
                down = True

            if down:
                x += 1
            else:
                x -= 1

        result = ''
        for x in str_list:
            for y in x:
                if y is not None:
                    result += y
        return result


if __name__ == '__main__':
    import time

    time.clock()
    s = 'yqmcmoeganjvsavkyxylqmnwbanzvfiwywymketmreijhfvhftsxfhthhjifqqbonbdzfymycujjbgsgzldhszqciyjyqmpfnsfuqruunfgolyvmlavezlihjtiafxfupmohdkdqpjhcieqtemzexjnjcvlhssbjfrsidwbuhiwpmnlsbkyawmjyjuieplpudieggfdnpzfdoqwrcwsyibzuyhynspjxxngfvjtmiaqzqoqskktvmspmbpbtekrexzjuiehsezrwnkrzukuielufavahhtlhswbadktjjmgyyxytjudpgauivupdqamiznjcaellqrmpqmkbgnqmnmxljmqznchmrsqrwbdnvreldopjbfyrsvcdhscwwjkncafycknzbrkefbpjjpadkcguwiqsrdhvfmwjyjibdthiwxtfmtizxotvwlpqqxlwlhfktonwjvgfualgvthtkcqgogwgdkcoriamyoihlpofpznkvvffxwnnemuhwwxpgacgoknbbegsdtfaokhoixbmjvvfuvwcvyjllymo'
    sol = Solution()
    print(sol.convert(s, 3))
    print(time.clock())
