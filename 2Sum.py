

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x = len(nums)
        for i in range(x-1):
            for j in range(1,x):
                if i == j:
                    continue
                if nums[i] + nums[j] == target:
                    return [i,j]
