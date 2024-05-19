class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count_s = {}
        count_t = {}
        for char in s:
            if char in count_s:
                count_s[char] += 1
            else:
                count_s[char] = 1
        for char in t:
            if char in count_t:
                count_t[char] += 1
            else:
                count_t[char] = 1
        common_count = 0
        for char in count_t:
            if char in count_s:
                common_count += min(count_s[char], count_t[char])

        return len(t) - common_count