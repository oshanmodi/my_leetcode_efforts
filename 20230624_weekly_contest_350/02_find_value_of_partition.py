from typing import List


class Solution:
    """
    https://leetcode.com/contest/weekly-contest-350/problems/find-the-value-of-the-partition/

    constraints:
    - 2 <= nums.length <= 105
    - 1 <= nums[i] <= 109
    """

    def findValueOfPartition(self, nums: List[int]) -> int:
        nums_sorted = sorted(nums)
        nums_sorted_shifted = nums_sorted[1:]
        difference = [nxt_val - val for val,nxt_val in zip(nums_sorted, nums_sorted_shifted)]
        # print(nums_sorted)
        # print(nums_sorted_shifted)
        # print(difference)
        print(min(difference))
        return(min(difference))


if __name__ == "__main__":
    sol = Solution()
    nums = [1,5,6,9,0,11,98]
    nums = [1,3,2,4]
    nums = [100, 1, 10]
    sol.findValueOfPartition(nums)
