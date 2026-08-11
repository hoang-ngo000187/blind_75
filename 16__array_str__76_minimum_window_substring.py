class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        minW = s
        LenS = len(s)
        countT, window = {}, {}

        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)

        left, right = 0, 0
        res, resLen = [-1, -1], float("infinity") # float("infinity") hay float("inf") dùng để tạo một giá trị số thực đại diện cho vô cực dương (∞)
        while(right < LenS):
            c = s[right]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                # update result
                cur_win_size = right - left + 1
                if cur_win_size < resLen:
                    res = [left, right]
                    resLen = cur_win_size
                # pop from the left of our window
                window[s[left]] -= 1
                if s[left] in countT and window[s[left]] < countT[s[left]]:
                    have -= 1
                left += 1
            right += 1
        start, stop = res
        return s[start: stop + 1] if resLen != float("infinity") else ""

if __name__ == '__main__':
    sol = Solution()
    s = "ADOBECODEBANC"
    t = "ABC"
    # s = "ADAOBBBECODEBANC" 
    # t = "AABBC" # Output: "BANC"
    print(sol.minWindow(s, t))