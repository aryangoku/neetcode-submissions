class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = {}
        for i in range(len(nums)):
            s = target - nums[i]
            if s in a:
                return [a[s], i]
            else:
                a[nums[i]] = i
        return b