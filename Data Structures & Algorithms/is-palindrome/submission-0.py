class Solution:
    def isPalindrome(self, s: str) -> bool:
        s= ''.join(s.split(" "))
        s=s.lower()
        i=0
        j=len(s)-1
        while i<j:
            if s[i].isalnum() and s[j].isalnum():
                if s[i]==s[j]:
                    i+=1
                    j-=1
                else:
                    return False
            else:
                if s[i].isalpha():
                    j-=1
                else:
                    i+=1
        return True 