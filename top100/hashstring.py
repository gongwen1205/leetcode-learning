# -*- coding: utf-8 -*-

class Solution:
    # 49. 字母异位词分组
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        for str in strs:
            sorted_str = ''.join(sorted(str))
            if sorted_str not in hash_map:
                hash_map[sorted_str] = []
            hash_map[sorted_str].append(str)
        return list(hash_map.values())
    
    # 128. 最长连续序列
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest_streak = 0
        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1
                longest_streak = max(longest_streak, current_streak)
        return longest_streak
    
