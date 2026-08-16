class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        next_greater = {}
        for num in nums2:
            while stack and stack[-1] < num:
                next_greater[stack[-1]] = num
                stack.pop()
            stack.append(num)

        for num in stack:
            next_greater[num] = -1
        return [next_greater[num] for num in nums1]

if __name__ == '__main__':
    sol = Solution()
    nums1 = [1,3,5,2,4]
    nums2 = [6,5,4,3,2,1,7]
    print(sol.nextGreaterElement(nums1, nums2))