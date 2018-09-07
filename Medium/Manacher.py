#!/usr/bin/env python

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = Solution.PreProcess(s)  #预处理
        p = []  #p数组，保存回文长度
        c = 0   #中心点位置，初始化为0
        r = 0   #右边界位置，初始化为0

    def PreProcess(s):
       """
       预处理过程，在字符串收尾插入^$ ，在字符串间插入#
       :param s: 待处理字符串
       :return: 处理完成的字符串
       """
       sList = list('^' + s + '$')
       return '#'.join(sList)


if __name__ == '__main__':
    s = 'cbbd'
    sl = Solution()
    print(sl.longestPalindrome(s))