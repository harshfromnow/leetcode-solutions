class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp=defaultdict(list)
        for word in strs:
            sortedw=''.join(sorted(word))
            mp[sortedw].append(word)
        return list(mp.values())