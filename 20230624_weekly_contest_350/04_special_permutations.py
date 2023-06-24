from typing import List
from itertools import permutations


class Solution:
    # https://leetcode.com/contest/weekly-contest-350/problems/special-permutations/
    # un-finished solution. 
    # Performance inadequate.
    def specialPerm(self, nums: List[int]) -> int:
        pairs = self.getPairs(nums)
        print(pairs)
        arrangements = permutations(nums,r = len(nums))
        special_permutations = [self.checkSpecialPerm(p) for p in arrangements]
        # print(len(special_permutations))
        total_special_permutations = sum(special_permutations)
        return int(total_special_permutations % (1e9 + 7))

    def checkSpecialPerm(self, nums: List[int]) -> bool:
        for i in range(len(nums) - 1):
            if (nums[i] % nums[i + 1] != 0) & (nums[i + 1] % nums[i]!=0):
                return False
        return True
    
    def getPairs(self, nums:List[int]) -> int:
        nums = sorted(nums)
        pairs = {}
        for i in range(len(nums)):
            pairs[nums[i]] = []
            for j in range(len(nums)):
                if (nums[i]!=nums[j]) & ((nums[i]%nums[j]==0)|(nums[j]%nums[i]==0)):
                    pairs[nums[i]].append(nums[j])
        num = sorted(nums, reverse=True)
        for i in range(len(nums)):
            pairs[nums[i]] = []
            for j in range(len(nums)):
                if (nums[i]!=nums[j]) & ((nums[i]%nums[j]==0)|(nums[j]%nums[i]==0)):
                    pairs[nums[i]].append(nums[j])
        return pairs
 
if __name__ == "__main__":
    sol = Solution()
    nums = [2, 3, 6]
    print(sol.specialPerm(nums))
    nums = [21,63,9,90,10,100,50,5,45,15]
    print(sol.specialPerm(nums))
