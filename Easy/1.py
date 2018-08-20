#!/usr/bin/env python


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if (nums[i] + nums[j]) == target:
                    return [i, j]


if __name__ == '__main__':
    S = Solution()
    Lst = [2, 7, 11, 15]
    print(S.twoSum(Lst, 9))
