from collections import Counter

class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:
        counts = Counter(s)
        groups = {}
        for letter, count in counts.items():
            if count not in groups:
                groups[count] = []
            groups[count].append(letter)
            
        ret = sorted(groups.items(), key = lambda x: (len(x[1]), x[0]), reverse = True)[0][1]
        return "".join(ret)
        
