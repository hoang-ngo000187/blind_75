"""
# First solution: Using Prefix Sum
import sys
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        L = len(nums)
        prefix_sum = [0]*(L+1)
        prefix_sum[0] = 0
        prefix_sum[1] = nums[0]
        for i in range(1, L):
            prefix_sum[i+1] = prefix_sum[i] + nums[i]
        avg_max = -sys.float_info.max
        for i in range(k-1, L):
            total_sum = prefix_sum[i+1] - prefix_sum[i+1-k]
            avg = float(total_sum / k)
            if avg > avg_max:
                avg_max = avg
        return avg_max
"""

# Second solution: Using Sliding Window
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        L = len(nums)
        # Sum for starting window
        current_sum = 0
        for i in range(k):
            current_sum += nums[i]
        
        max_sum = current_sum
        
        # Start sliding window
        start_index = 0
        end_index = k
        while(end_index < L):
            # Remove previous element
            current_sum -= nums[start_index]
            start_index += 1

            # Add next element
            current_sum += nums[end_index]
            end_index += 1

            # Update max sum
            if current_sum > max_sum:
                max_sum = current_sum
        
        # Return the average
        return float(max_sum/k)

if __name__ == '__main__':
    sol = Solution()
    nums = [1,12,-5,-6,50,3]
    k = 4
    print(sol.findMaxAverage(nums, k))