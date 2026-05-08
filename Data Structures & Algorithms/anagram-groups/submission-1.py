class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        collect = defaultdict(list)

        for strings in strs:
            sortedword = sorted(strings)
            key = ''.join(sortedword)
            collect[key].append(strings)

        
        return list(collect.values())