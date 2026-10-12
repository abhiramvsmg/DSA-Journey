class Solution:
    def minWindow(self, s, t):
        need = {}
        for char in t:
            need[char] = need.get(char, 0) + 1

        window = {}
        left = 0
        have = 0
        required = len(need)
        start = 0
        min_length = float("inf")

        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char, 0) + 1

            if char in need and window[char] == need[char]:
                have += 1

            while have == required:
                length = right - left + 1

                if length < min_length:
                    min_length = length
                    start = left

                left_char = s[left]
                window[left_char] -= 1

                if left_char in need and window[left_char] < need[left_char]:
                    have -= 1

                left += 1

        if min_length == float("inf"):
            return ""

        return s[start:start + min_length]
