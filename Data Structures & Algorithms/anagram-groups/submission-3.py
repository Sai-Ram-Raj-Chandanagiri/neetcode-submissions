class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        Approach : Using Sorting
        Sort all the strings and map all the strings that match the sorted string.
        In the end return all the values in a single list.
        '''
        res = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            res[sortedS].append(s)
        return list(res.values())