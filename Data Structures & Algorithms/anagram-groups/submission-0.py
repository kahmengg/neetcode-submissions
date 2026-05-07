class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for words in strs:
            sorted_word = sorted(words)
            key = ''.join(sorted_word)

            hashmap[key].append(words)
        
        return list(hashmap.values())