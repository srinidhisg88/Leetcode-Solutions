from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # Initialize result list and partition list
        res = []
        part = []

        # Backtracking function (DFS)
        def dfs(i):
            # If the current index is beyond the string, append the partition to the result
            if i >= len(s):
                res.append(part.copy())
                return
            # Iterate over all possible substrings starting from index i
            for j in range(i, len(s)):
                if self.ispali(s, i, j):  # If the substring is a palindrome
                    part.append(s[i:j+1])  # Add the substring to the current partition
                    dfs(j+1)  # Recur for the next index
                    part.pop()  # Backtrack by removing the last added substring

        # Call the DFS function starting from index 0
        dfs(0)
        return res

    # Helper function to check if a substring is a palindrome
    def ispali(self, s: str, i: int, j: int) -> bool:
        while i < j:
            if s[i] != s[j]:
                return False
            i, j = i + 1, j - 1
        return True
