class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = []
        r = []
        output = []

        multiplier = 1
        for i, val in enumerate(nums):
            if i != 0:
                multiplier *= nums[i - 1]
            l.append(multiplier)

        multiplier = 1
        rnums = list(reversed(nums))
        for i, val in enumerate(rnums):
            if i != 0:
                multiplier *= rnums[i - 1]
            r.insert(0, multiplier)

        for x, y in zip(l, r):
            output.append(x * y)

        return output