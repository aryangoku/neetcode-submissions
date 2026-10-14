class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a = {}
        for i in range(len(nums)):
            if nums[i] in a:
                return True
            else:
                a[nums[i]] = a.get(nums[i], 0) + 1
        return False