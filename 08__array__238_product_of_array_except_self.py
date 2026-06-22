class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Input: nums = [1,2,3,4]
        
        left = [1,2,6,24]
        right = [24 , 24, 12, 4]

        Output: [24,12,8,6]
        """
        L = len(nums)
        prefix_left = [1]*L
        prefix_right = [1]*L
        result = [1]*L
        prefix_left[0] = nums[0]
        for i in range(L):
            prefix_left[i] = prefix_left[i-1] * nums[i]
        
        prefix_right[L-1] = nums[L-1]
        for i in reversed(range(0, L-1)):
            prefix_right[i] = prefix_right[i+1] * nums[i]
        
        for i in range(L):
            if i == 0:
                result[i] = prefix_right[i+1]
            elif i == L-1:
                result[i] = prefix_left[i-1]
            else:
                result[i] = prefix_left[i-1]*prefix_right[i+1]
        return result

if __name__ == '__main__':
    sol = Solution()
    print(sol.productExceptSelf([1,2,3,4]))
