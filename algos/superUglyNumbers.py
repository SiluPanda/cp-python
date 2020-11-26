import heapq

class Solution:
    def nthSuperUglyNumber(self, n: int, primes):
        min_heap = []
        ret = [1]
        for i in range(len(primes)):
            heapq.heappush(min_heap, primes[i])
        while len(ret) < n:
            curr_num = heapq.heappop(min_heap)
            ret.append(curr_num)
            if len(min_heap) > 0:
                second = heapq.heappop(min_heap)
                heapq.heappush(min_heap, second * curr_num)
                heapq.heappush(min_heap, second)
            heapq.heappush(min_heap, curr_num )
        print(ret)
        return ret[n-1]
        



sol = Solution()
n = int(input())
primes = [int(s) for s in input().split()]
print(sol.nthSuperUglyNumber(n, primes))