class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Apparent Optimal Solution
        counts = {}
        for c in s:
            counts[c] = counts.get(c, 0) + 1
        for c in t:
            counts[c] = counts.get(c, 0) - 1

        return all(v == 0 for v in counts.values())