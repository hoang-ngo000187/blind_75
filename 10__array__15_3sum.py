class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []
        nums.sort()
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            if i > 0 and nums[i] == nums[i-1]:
                    continue
            while (left < right):
                total = nums[i] + nums[left] + nums[right]
                if (total == 0):
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]: left += 1
                    while left < right and nums[right] == nums[right+1]: right -= 1
                elif (total < 0):
                    left += 1
                else: # (total > 0):
                    right -= 1
        return result


if __name__ == '__main__':
    sol = Solution()
    # nums = [1,2,0,1,0,0,0,0]
    # nums = [-2,0,1,1,2]
    nums = [-1,0,1,2,-1,-4,-2,-3,3,0,4]
    print(sol.threeSum(nums))
