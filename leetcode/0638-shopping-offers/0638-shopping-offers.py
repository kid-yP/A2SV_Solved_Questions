class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        n = len(price)
        valid_specials = []
        for sp in special:
            total = sum(sp[i] * price[i] for i in range(n))
            if total > sp[n]:
                valid_specials.append(sp)

        memo = {}

        def dfs(state):
            if state in memo:
                return memo[state]

            cost = sum(state[i] * price[i] for i in range(n))

            for sp in valid_specials:
                new_state = list(state)
                ok = True
                for i in range(n):
                    if sp[i] > new_state[i]:
                        ok = False
                        break
                    new_state[i] -= sp[i]
                if ok:
                    cost = min(cost, sp[n] + dfs(tuple(new_state)))

            memo[state] = cost
            return cost

        return dfs(tuple(needs))