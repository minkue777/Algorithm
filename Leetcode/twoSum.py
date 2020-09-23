from typing import *

def twoSum(nums: List[int], target: int) -> List[int]:
    checked_diff = dict()
    for i in range(len(nums)):
        if nums[i] in checked_diff:
            return [checked_diff[nums[i]], i]
        diff = target - nums[i]
        checked_diff[diff] = i

if __name__ == '__main__':
    sol = twoSum([3, 2, 4], 6)
    print(sol)