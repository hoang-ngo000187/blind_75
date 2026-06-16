class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Fill frequencyMap
        hash_map = {}
        for x in nums:
            if x not in hash_map:
                hash_map[x] = 1
            else:
                hash_map[x] += 1

        # Fill bucket
        bucket = [[] for _ in range(len(nums) + 1)]
        for key, value in hash_map.items():
            bucket[value].append(key)
        
        ret = []
        # Iterate bucket in reverse to get top k frequent elements
        for i in reversed(range(len(bucket))):
            if bucket[i] != []:
                ret.extend(bucket[i])
            if len(ret) == k:
                break
        
        return ret



if __name__ == '__main__':
    sol = Solution()
    ret = sol.topKFrequent([1,2,1,2,1,2,3,1,3,2], 2)
    print(ret)
