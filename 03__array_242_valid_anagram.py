class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        s = s.replace(" ", "")
        t = t.replace(" ", "")
        
        if len(s) != len(t):
            return False

        counts = [0]*26
        for char in s:
            counts[ord(char) - ord('a')] += 1
        for char in t:
            counts[ord(char) - ord('a')] -= 1
        for num in counts:
            if num != 0:
                return False
        return True

if __name__ == '__main__':
    sol = Solution()
    s = "school master"
    t = "the classroom"
    ret = sol.isAnagram(s, t)
    print(ret)