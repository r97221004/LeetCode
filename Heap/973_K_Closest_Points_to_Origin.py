import heapq


class Solution:
    def kClosest(self, points, k):
        pts = [[(x**2 + y**2), x, y] for x, y in points]
        heapq.heapify(pts)

        res = []
        for _ in range(k):
            dis, x, y = heapq.heappop(pts)
            res.append([x, y])

        return res
