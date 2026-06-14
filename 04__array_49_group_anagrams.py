class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []
        
        hash_map = {}
        
        def generate_frequent_pattern(element):
            freq_list = [0] * 26
            
            for char in element:
                freq_list[ord(char) - ord('a')] += 1
            
            cur_char = 'a'
            pattern = ""
            for position in freq_list:
                pattern += cur_char
                pattern += str(position)
                cur_char = chr(ord(cur_char) + 1)
            return pattern
        
        for s in strs:
            freq_pattern = generate_frequent_pattern(s)
            if freq_pattern not in hash_map:
                hash_map[freq_pattern] = [s]
            else:
                hash_map[freq_pattern].append(s)

        return list(hash_map.values())


if __name__ == '__main__':
    sol = Solution()
    ret = sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    print(ret)

