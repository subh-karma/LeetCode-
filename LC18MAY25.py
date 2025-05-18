class Solution:
    MOD = 10**9 + 7

    def colorTheGrid(self, m: int, n: int) -> int:
        def generate_states(pos=0, curr=[]):
            if pos == m:
                states.append(tuple(curr))
                return
            for color in range(1, 4):
                if pos == 0 or curr[-1] != color:
                    generate_states(pos + 1, curr + [color])

        def is_compatible(a, b):
            return all(x != y for x, y in zip(a, b))

        states = []
        generate_states()

        index = {state: i for i, state in enumerate(states)}
        size = len(states)
        transitions = [[] for _ in range(size)]

        for i in range(size):
            for j in range(size):
                if is_compatible(states[i], states[j]):
                    transitions[i].append(j)

        dp = [1] * size
        for _ in range(1, n):
            new_dp = [0] * size
            for i in range(size):
                for j in transitions[i]:
                    new_dp[j] = (new_dp[j] + dp[i]) % self.MOD
            dp = new_dp

        return sum(dp) % self.MOD
