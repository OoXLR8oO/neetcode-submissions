class Solution:
    def tribonacci(self, n: int) -> int:
        first  = 0
        second = 1
        third  = 1

        for i in range(n):
            first, second, third  = second, third, first + second + third
        
        return first

