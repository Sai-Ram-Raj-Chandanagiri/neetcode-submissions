class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #From Hint-1:
        d={}
        for string in strs:
            key = ''.join(sorted(string))
            if key in d:
                d[key].append(string)
            else:
                d[key]=[string]
        final_list=[]
        for i in d.keys():
            final_list.append(d[i])
        return final_list