class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_list_1=[]
        group_dict = {}
        group_list_2=[]
        def count_dict(s:str):
            d={}
            for i in range(len(s)):
                if s[i] in d:
                    d[s[i]]+=1
                else:
                    d[s[i]]=1
            return d
        for i in range(len(strs)):
            a= count_dict(strs[i])
            if a not in group_list_1:
                group_list_1.append(a)
                group_dict[len(group_list_1)]=a
                group_list_2.append([strs[i]])
            else:
                for j in group_dict:
                    if group_dict[j] == a:
                        group_list_2[j-1]+=[strs[i]]
        return group_list_2