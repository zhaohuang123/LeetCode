#!/usr/bin/env python

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        #采用动态规划的方法
        DPMa = [[0 for i in range(len(s))] for j in range(len(s))]  #初始化二维矩阵，用户动态规划预计算

        LenPa = 1
        iMax = jMax = 0
        for i in range(len(s)):
            DPMa[i][i] = 1
            if i + 1 < len(s) and s[i] == s[i + 1]:#出现相同两位的回文字符串
                DPMa[i][i + 1] = 1
                LenPa = 2
                iMax = i
                jMax = i + 1
        for k in range(2, len(s)):
            for i in range(0, len(s) - k):
                j = i + k
                if DPMa[i + 1][j - 1] and s[i] == s[j]:
                    DPMa[i][j] = 1
                    if k + 1 > LenPa:
                        LenPa = k + 1
                        iMax = i
                        jMax = j

        return s[iMax:jMax + 1]


if __name__ == '__main__':
    s = 'cbbd'
    sl = Solution()
    print(sl.longestPalindrome(s))