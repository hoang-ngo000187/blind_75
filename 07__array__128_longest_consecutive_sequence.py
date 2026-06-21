class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_map = {}
        for num in nums:
            hash_map[num] = False
        max_len = 0
        tmp = 0
        for num in nums:
            if hash_map[num] == False:
                hash_map[num] = True
                tmp = 1
                # Forward
                next = num + 1
                while(next in hash_map):
                    hash_map[next] = True
                    next = next + 1
                    tmp += 1
                # Backward
                next = num - 1
                while(next in hash_map):
                    hash_map[next] = True
                    next = next -1
                    tmp += 1
                if tmp > max_len:
                    max_len = tmp
        return max_len

if __name__ == '__main__':
    sol = Solution()
    print(sol.longestConsecutive([]))
