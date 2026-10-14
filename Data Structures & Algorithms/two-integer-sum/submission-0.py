class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = {}
        b = []
        for i in range(len(nums)):
            s = target - nums[i]
            if s in a:
                b.append(a[s])
                b.append(i)
            else:
                a[nums[i]] = i
        return b