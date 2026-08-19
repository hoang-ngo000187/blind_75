EFFICIENT = 0

if EFFICIENT:
    print("Continue ... ... ...")
else:
    class Solution:
        SIGN = {'+': 1, '-': -1, '*': 2, '/': 3}
        def char2int(self, c: char) -> int:
            return (ord(c) - ord('0'))

        def calculate(self, s: str) -> int: # s = "9*11 + 88/44 -18 + 30"
            stack = []
            tmp = 0
            wait = False
            num_read = True
            sign = 1
            s += '+'
            for c in s:
                if c == " ":
                    continue
                elif c not in self.SIGN:
                    if num_read and stack:
                        tmp = stack.pop()
                    else:
                        tmp = 0
                    num_read = True
                    tmp = tmp * 10 + self.char2int(c)
                    stack.append(tmp)
                else:
                    tmp = 0
                    num_read = False
                    if wait:
                        wait = False
                        num1 = stack.pop()
                        num2 = stack.pop()
                        if sign == 2:
                            ret = num2 * num1
                        else:
                            ret = int(num2 / num1)
                        stack.append(ret)
                    else:
                        stack[-1] *= sign
                    sign = self.SIGN[c]
                    if sign == 2 or sign == 3:
                        wait = True
            result = 0
            for num in stack:
                result += num
            return result

if __name__ == '__main__':
    sol = Solution()
    # s = "   12 + 18 - 5 - 2* 3"
    # s = "0-2147483647"
    # s = "14/3*2"
    # s = "1*2-3/4+5*6-7*8+9/10"
    # s = "9*11 + 88/44 -18  *30"
    # s = "32+42"
    s = "14-3/2"
    print(sol.calculate(s))