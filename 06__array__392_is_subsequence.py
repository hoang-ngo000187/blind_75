class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ls = len(s)
        lt = len(t)
        if (ls > lt):
            return False

        if (ls == 0):
            return True

        i = 0
        j = 0
        while(j < lt):
            if t[j] == s[i]:
                i += 1
                if i == ls:
                    return True
            j += 1
        return False
        
if __name__ == '__main__':
    sol = Solution()
    print(sol.isSubsequence("aaaaaa", "bbaaaa"))
