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

#New
# class Solution:
#     def isValid(self, s: str) -> bool:
#         stack = []
#         pairs = {')': '(', '}': '{', ']': '['}
#         for c in s:
#             if c in pairs and (not stack or stack.pop() != pairs[c]):
#                 return False
#             elif c in '([{':
#                 stack.append(c)
#         return not stack
