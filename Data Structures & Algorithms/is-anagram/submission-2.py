class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def create_count_d(string: str):
            d={}
            for i in range(len(string)):
                if string[i] in d:
                    d[string[i]]+=1
                else:
                    d[string[i]]=1
            return d
        s_d = create_count_d(s)
        t_d = create_count_d(t)

        if s_d == t_d:
            return True
        else:
            return False
            