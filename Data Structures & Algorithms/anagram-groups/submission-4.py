class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        Approach-3: Using hasmaps but way easier:
        Use a 26 length tuple to maintain the freqency of the alphabets 
        and them match and club using this as tuples can be used as keys in dict.
        '''
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())