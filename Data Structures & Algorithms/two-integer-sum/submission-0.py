class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for x in range (len(nums)):
            curr = nums[x]
            for y in range(x+1, len(nums)):
                if curr + nums[y] == target:
                    return [y,x] if x > y else [x,y]