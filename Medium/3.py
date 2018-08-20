class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        low = 0
        Map = {}
        MaxLengh = 0
        for high in range(0, len(s)):
            if s[high] in Map:   #如果出现重复字符串
                while s[low] != s[high]:
                    Map.pop(s[low])
                    low += 1
                Map[s[high]] = high
                low += 1
            else:
                Map[s[high]] = high
            high += 1
            if (high - low) > MaxLengh:
                MaxLengh = high - low
        return MaxLengh

        # Length = len(s)
        # if Length == 0:
        #     return 0
        # low = 0
        # high = 1
        # Map = {}
        # MaxLengh = 1
        # Map[s[low]] = low
        # while high < Length:
        #     if s[high] in Map:   #如果出现重复字符串
        #         while s[low] != s[high]:
        #             Map.pop(s[low])
        #             low += 1
        #         Map[s[high]] = high
        #         low += 1
        #     else:
        #         Map[s[high]] = high
        #     high += 1
        #     if (high - low) > MaxLengh:
        #         MaxLengh = high - low
        #
        # return MaxLengh

if __name__ == '__main__':
    #s = 'abcabcbb'
    #s = 'pwwkew'
    s = ''
    Slo = Solution()
    print(Slo.lengthOfLongestSubstring(s))
