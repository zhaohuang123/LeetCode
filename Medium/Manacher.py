#!/usr/bin/env python

class Solution:
    def longestPalindrome(self, s):
        s = Solution.PreProcess(s)  #预处理
        P = [0] * (len(s))  #p数组，保存回文长度
        C = 0   #中心点位置，初始化为0
        R = 0   #右边界位置，初始化为0
        for i in range(1, len(s) - 1):
            iMirror = 2*C - i
            if iMirror < 0:
                iMirror = 0
            # 计算在当前以C为中心的的最大对称位置
            P[i] = min(R - i, P[iMirror]) if R > i else 0
            # 对边界进行扩展，利用循环对边界进行扩展
            while (s[i - 1 - P[i]] == s[i + 1 + P[i]]):
                P[i] += 1
            # 计算新的C和R的位置
            if (i + P[i] > R):
                R = i + P[i]
                C = i

        MaxLen = max(P)
        index = P.index(MaxLen)
        return s[index - MaxLen: index + MaxLen + 1].replace('#', '')


    def PreProcess(s):
       """
       预处理过程，在字符串收尾插入^$ ，在字符串间插入#
       :param s: 待处理字符串
       :return: 处理完成的字符串
       """
       sList = list('^' + s + '$')
       return '#'.join(sList)


if __name__ == '__main__':
    # s = 'cbbd'
    # s = "babcbabcbaccba"
    s = ""
    sl = Solution()
    print(sl.longestPalindrome(s))