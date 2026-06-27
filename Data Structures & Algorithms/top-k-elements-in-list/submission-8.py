class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
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
        print(final_keys, rev_freq)
        while len(final)<k:
            final+=rev_freq[final_keys.pop()]
        return final