from collections import deque

class Solution:
    def deckRevealedIncreasing(self, deck):
        N = len(deck)
        T = deque(range(N))
        deck.sort()
        ret = [-1 for i in range(N)]
        for i in range(N):
            curr_index = T.popleft()
            ret[curr_index] = deck[i]
            if T:
                T.append(T.popleft())
        return ret
            


sol = Solution()
deck = [int(s) for s in input().split(' ')]
print(sol.deckRevealedIncreasing(deck))