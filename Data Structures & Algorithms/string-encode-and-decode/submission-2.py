class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string=""
        for i in strs:
            encoded_string+=i+"solvingtheproblem"
        return encoded_string
    def decode(self, s: str) -> List[str]:
        return s.split("solvingtheproblem")[:-1]