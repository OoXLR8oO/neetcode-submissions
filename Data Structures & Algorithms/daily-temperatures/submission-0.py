class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temps = temperatures
        n = len(temps)
        answer = [0] * n
        stack = []

        for i, temp in enumerate(temps):
            while stack and stack[-1][0] < temp:
                stk_t, stk_i = stack.pop()
                answer[stk_i] = i - stk_i

            stack.append((temp, i))

        return answer

