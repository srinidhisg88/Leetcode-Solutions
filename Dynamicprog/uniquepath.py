class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # Check for edge cases
        if not obstacleGrid or obstacleGrid[0][0] == 1:
            return 0
        
        # Get dimensions of the grid
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        # Create the DP table initialized to 0
        dp = [[0 for _ in range(n)] for _ in range(m)]
        
        # Initialize the first cell
        dp[0][0] = 1
        
        # Fill the DP table
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0  # If there's an obstacle, no paths through this cell
                else:
                    if i > 0:
                        dp[i][j] += dp[i-1][j]  # Paths from the cell above
                    if j > 0:
                        dp[i][j] += dp[i][j-1]  # Paths from the cell to the left
        
        # Return the value in the bottom-right corner
        return dp[m-1][n-1]
