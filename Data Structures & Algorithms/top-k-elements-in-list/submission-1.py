class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        seen = set()
        lst = []
        for n in range (len(nums)): 
            if nums[n] not in seen:
                seen.add(nums[n])
                count[nums[n]] = 1
            else:    
                count[nums[n]] = 1 + count.get(nums[n], 0)
        for x in range(k):
            max_key = max(count, key = count.get)
            lst.append(max_key)
            count.pop(max_key)
        return lst