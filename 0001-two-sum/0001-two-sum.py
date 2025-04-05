class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevDict = {}
        for idx,num in enumerate(nums):
            diff = target - num
            if diff in prevDict:
                return [prevDict[diff],idx]
            prevDict[num] = idx