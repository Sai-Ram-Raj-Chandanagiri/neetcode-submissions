class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # #BruteForce
        # s = sorted(s)
        # t = sorted(t)
        # return s==t

        #Optimal Solution
        def creatingDict(a:str):
            d={}
            for i in a:
                if i in d.keys():
                    d[i]+=1
                else:
                    d[i]=1
            return d
        return creatingDict(s) == creatingDict(t)