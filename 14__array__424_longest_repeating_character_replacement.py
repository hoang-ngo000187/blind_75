class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L = len(s)
        freq = [0]*26
        freq[ord(s[0]) - ord("A")] += 1
        max_freq = 1 # Equal to the frequency of first element
        max_len = 1 # Contain only first element
        # Left and right pointer point to first element at the begining
        left = 0 
        right = 0

        while (True):
            cur_len = right - left + 1 # Find the current window size
            if cur_len - max_freq <= k: # Check if the window is valid or not
                max_len = max(max_len, cur_len) # If the window is valid, update max len
                right += 1 # Then, extend the size of it
                # Exceed the range or not ?
                if right < L:
                    freq[ord(s[right]) - ord("A")] += 1
                    new_freq = freq[ord(s[right]) - ord("A")]
                    max_freq = max(max_freq, new_freq)
                else:
                    break
            else: # Decrease window size by removing element of window on the left
                freq[ord(s[left]) - ord("A")] -= 1
                left += 1
                
        return max_len

if __name__ == '__main__':
    sol = Solution()
    s = "ABAB"
    k = 2
    print(sol.characterReplacement(s, k))