class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        area = 0
        MAXarea = 0
        i = 0
        j = len(height) - 1
        while(j>i):
            if(height[i] <= height[j]):
                area = height[i]*(j - i)
                i += 1
            else:
                area = height[j]*(j - i)
                j -= 1
            MAXarea = max(area, MAXarea)

        return MAXarea
    
if __name__ == '__main__':
    sol = Solution()
    height = [1,8,6,2,5,4,8,3,7]
    print(sol.maxArea(height))