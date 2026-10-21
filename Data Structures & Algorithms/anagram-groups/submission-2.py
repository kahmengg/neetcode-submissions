class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        

        group = {}
        for word in strs:
            freq = [0] * 26

            for letter in word:
                freq[ord(letter) - ord('a')] += 1

            key = tuple(freq)

            if key not in group:
                group[key] = []

            group[key].append(word)
        return list(group.values())
            
            

            

