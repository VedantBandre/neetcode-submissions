class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list) # mapping character count of each string to the list of anagrams

        for s in strs:
            count = [0] * 26 # a to z
            
            for c in s:
                count[ord(c) - ord("a")] += 1
            # print(count)
            result[tuple(count)].append(s)
        
        # print(result.keys())
        return list((result.values()))