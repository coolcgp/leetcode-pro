class Solution(object):
    def climbStairs(self, n):

        if n <= 0:
            return 0

        cache = list()
        cache.insert(0, 1)
        cache.insert(1, 1)
        for i in range(2, n + 1):
            cache.insert(i, cache[i - 1] + cache[i - 2])
        return cache[n]


solution = Solution()
rst = solution.climbStairs(2)
print(rst)
