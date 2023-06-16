from typing import List
# Brute force
class Solution:

    def twoSumBF(self, nums: List[int], target:int)-> List[int]:
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
        return []

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numToIndex = {}
        for i in range(len(nums)):
            if (target - nums[i]) in numToIndex:
                return [numToIndex[target- nums[i]], i]
            numToIndex[nums[i]] = i
        return []


if __name__ == "__main__":
    sol = Solution()
    nums = list(range(100))
    target = 77
    print(sol.twoSumBF(nums, target))
    print(sol.twoSum(nums, target))