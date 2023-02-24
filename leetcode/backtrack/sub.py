from typing import List


def subsetsWithDup(nums: List[int]) -> List[List[int]]:

    nums.sort()
    result = []

    def backtrack(pos, curr_nums):
        if(pos == len(nums)):
            result.append(curr_nums.copy())
            return

        curr_nums.append(nums[pos])
        backtrack(pos+1, curr_nums)
        curr_nums.pop()

        while(pos+1 < len(nums) and nums[pos] == nums[pos+1]):
            pos += 1

        backtrack(pos+1, curr_nums)

    backtrack(0, [])
    return result


print(subsetsWithDup([1, 2, 2]))
