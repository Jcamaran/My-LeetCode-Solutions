class Solution(object):
    def moveZeroes(self, nums):
        zeroes = []

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == 0:
                nums.pop(i)
                zeroes.append(0)

        nums.extend(zeroes)

        return nums
