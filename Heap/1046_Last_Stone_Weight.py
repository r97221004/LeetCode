import heapq


class Solution:
    def lastStoneWeight(self, stones):
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            first, second = heapq.heappop(stones), heapq.heappop(stones)
            if second > first:
                heapq.heappush(stones, first - second)

        if stones:
            return -stones[0]
        return 0
