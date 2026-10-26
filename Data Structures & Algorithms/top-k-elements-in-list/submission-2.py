class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for x in range(len(nums) + 1)]
        
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, val in count.items():
            freq[val].append(num)
        
        res = []
        for x in range(len(freq)-1, 0, -1):
            for n in freq[x]:
                res.append(n)
                if(len(res) == k):
                    return res