import heapq

class Solution:
    def maxProfit(self, inventory, orders) -> int:
        max_heap = []
        for x in inventory:
            heapq.heappush(max_heap, -x)
        ret = 0
        while orders:
            curr = heapq.heappop(max_heap)
            print(curr)
            ret += curr * -1
            heapq.heappush(max_heap, curr + 1)
            orders -= 1
        return ret

sol = Solution()
inventory = [int(s) for s in input().split()]
orders = int(input())
print(sol.maxProfit(inventory, orders))