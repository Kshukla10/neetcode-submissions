class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = {}

        for index, num in enumerate(nums):
            complement = target - num
            if complement in result:
                return [result[complement], index]
            result[num] = index