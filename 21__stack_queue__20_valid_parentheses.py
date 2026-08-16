class Solution:
    def isValid(self, s: str) -> bool:
        mapping_bracket = { 
            ')': '(',
            '}': '{',
            ']': '[',
         }

        stack = []

        for char in s:
            if char in mapping_bracket:
                if stack: # check for case s = "]" and at this time, stack still []
                    top_element = stack.pop()
                else:
                    top_element = "!"
                
                if top_element != mapping_bracket[char]:
                    return False
            else:
                stack.append(char)
        return (len(stack) == 0)

if __name__ == '__main__':
    sol = Solution()
    s_testcase = ["()",
                  "()[]{}",
                  "(]",
                  "([])",
                  "([)]",
                  "]"]
    for i, testcase in enumerate(s_testcase):
        print(f"Testcase{i}: {testcase} -> Result: {sol.isValid(testcase)}\n")

"""
PS D:\Workspace\WS_LEETCODE\blind_75>  & 'C:\Users\LENOVO\AppData\Local\Python\pythoncore-3.14-64\python.exe' 'c:\Users\LENOVO\.vscode\extensions\ms-python.debugpy-2026.6.0-win32-x64\bundled\libs\debugpy\launcher' '53940' '--' 'D:\Workspace\WS_LEETCODE\blind_75\21__stack_queue__20_valid_parentheses.py' 
Testcase0: () -> Result: True

Testcase1: ()[]{} -> Result: True

Testcase2: (] -> Result: False

Testcase3: ([]) -> Result: True

Testcase4: ([)] -> Result: False

Testcase5: ] -> Result: False
"""