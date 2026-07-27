class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_map = {}
        max_len = 0
        left = right = 0
        L = len(s)
        if L == 0:
            return 0

        while(right < L):
            if hash_map.get(s[right], 0) == 0:
                hash_map[s[right]] = 1
                max_len = max(max_len, (right - left + 1))
                right += 1
            else:
                hash_map[s[left]] = 0
                left += 1
        return max_len

if __name__ == '__main__':
    sol = Solution()
    s = "pwwkew"
    print(sol.lengthOfLongestSubstring(s))