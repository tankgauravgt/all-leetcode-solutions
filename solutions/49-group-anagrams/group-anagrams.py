from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = defaultdict(list)
        for s in strs:
            temp = dict(Counter(s))
            hash_key = []
            for c in 'abcdefghijklmnopqrstuvwxyz':
                hash_key.append(f"{c}{temp.get(c, 0)}")
            groups["".join(hash_key)].append(s)
        
        return list(groups.values())