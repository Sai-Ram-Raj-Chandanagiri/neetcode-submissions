class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #A better version of Solution-1

        if len(s)!=len(t):
            return False
        d_s={}
        d_t={}
        for i in range(len(s)):
            if s[i] in d_s:
                d_s[s[i]]+=1
            else : d_s[s[i]]=1

            if t[i] in d_t:
                d_t[t[i]]+=1
            else: d_t[t[i]]=1
        if d_s != d_t:
            return False
        return True