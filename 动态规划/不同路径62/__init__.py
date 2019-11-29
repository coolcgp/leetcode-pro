class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0 for i in range(n)] for j in range(m)]

        for i in range(0, m):
            dp[i][0] = 1

        for j in range(0, n):
            dp[0][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]


m = 3
n = 2
solution = Solution()
rst = solution.uniquePaths(m, n)
print(rst)
