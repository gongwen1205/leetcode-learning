# -*- coding: utf-8 -*-

class Solution:
    # 3. 无重复字符的最长子串
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_length = 0
        last_seen = {}

        for right, char in enumerate(s):
            if char in last_seen and last_seen[char] >= left:
                left = last_seen[char] + 1
            last_seen[char] = right
            max_length = max(max_length, right - left + 1)

        return max_length
    
    # 438. 找到字符串中所有字母异位词
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        if len(p) > len(s):
            return result

        left = 0
        right = 0
        valid = 0
        window = {}
        need = {}
        for char in p:
            need[char] = need.get(char, 0) + 1

        while right < len(s):
            char = s[right]
            right += 1
            if char in need:
                window[char] = window.get(char, 0) + 1
                if window[char] == need[char]:
                    valid += 1

            if right - left == len(p):
                if valid == len(need):
                    result.append(left)
                char = s[left]
                left += 1
                if char in need:
                    if window[char] == need[char]:
                        valid -= 1
                    window[char] -= 1

        return result

    # 239. 滑动窗口最大值
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        result = []
        dq = deque()  # 存下标，队首对应当前窗口最大值

        for i, num in enumerate(nums):
            while dq and dq[0] <= i - k:
                dq.popleft()
            while dq and nums[dq[-1]] <= num:
                dq.pop()
            dq.append(i)
            if i >= k - 1:
                result.append(nums[dq[0]])

        return result

    # 76. 最小覆盖子串
    ```
    思路need：统计 t 中每个字符需要的数量
    1. 右指针扩张：把字符加入 window，某字符在窗口内的数量达到 need 时，valid += 1
    2. 左指针收缩：当 valid == len(need)（窗口已覆盖 t）时，尝试缩小窗口并更新最短答案
    3. valid 减少：左端移出的字符若在 need 中，且移出前刚好满足需求，则 valid -= 1
    ```
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ''
        left = 0
        right = 0
        valid = 0
        start = 0
        min_len = float('inf')
        window = {}
        need = {}
        for char in t:
            need[char] = need.get(char, 0) + 1

        while right < len(s):
            char = s[right]
            right += 1
            if char in need:
                window[char] = window.get(char, 0) + 1
                if window[char] == need[char]:
                    valid += 1
            while valid == len(need):
                if right - left < min_len:
                    start = left
                    min_len = right - left
                char = s[left]
                left += 1
                if char in need:
                    if window[char] == need[char]:
                        valid -= 1
                    window[char] -= 1
        return s[start:start+min_len] if min_len != float('inf') else ''    