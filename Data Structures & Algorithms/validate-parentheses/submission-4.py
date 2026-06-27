class Solution:
    def isValid(self, s: str) -> bool:
        l=[]
        for i in range(len(s)):
            if s[i] in "({[":
                l.append(s[i])
            else:
                if len(l)==0:
                    return False
                char=l.pop()
                if s[i]=="}" and char=="{":
                    continue
                if s[i]==")" and char=="(":
                    continue
                if s[i]=="]" and char=="[":
                    continue
                else:
                    return False
        if len(l)==0:
            return True
        else:
            return False