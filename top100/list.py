# -*- coding: utf-8 -*-

from typing import List


class Solution:
    # 56. 合并区间
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged

    # 189. 旋转数组
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n
        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])

    # 238. 除自身以外数组的乘积
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n
        left = 1
        right = 1
        for i in range(n):
            result[i] *= left
            left *= nums[i]
            result[n - i - 1] *= right
            right *= nums[n - i - 1]
        return result
