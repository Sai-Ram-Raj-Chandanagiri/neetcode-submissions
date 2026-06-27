class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Approach create a freq dictionary and a reverse freqency dictioary in which we will put values as lists as the freqency can be duplicates. Then we will take the keys of the rev_frequency dictionary sort them in final_keys list and then pop from end till the list 
        if len(nums)==k:
            return nums
        freq={}
        for i in range(len(nums)):
            if nums[i] in freq:
                freq[nums[i]]+=1
            else:
                freq[nums[i]]=1
        rev_freq={}
        for i in freq:
            if freq[i] in rev_freq:
                rev_freq[freq[i]]+=[i]
            else:
                rev_freq[freq[i]] = [i]
        final_keys = sorted(rev_freq.keys())
        final=[]
        while len(final)<k:
            final+=rev_freq[final_keys.pop()]
        return final[:k]