from typing import List

class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        arr = [0] * (2 * n - 1)
        used = [False] * (n + 1)  # To track used numbers (1 to n)

        def generateSub(i):
            if i == len(arr):  # Base case: sequence completed
                return True
            if arr[i] != 0:  # Skip filled positions
                return generateSub(i + 1)
            
            for num in range(n, 0, -1):  # Try placing largest available number first
                nextindex = i if num == 1 else (i + num)  # Compute position for second occurrence
                
                if used[num] or (num > 1 and (nextindex >= len(arr) or arr[nextindex] != 0)):
                    continue  # Skip if number is used or position is invalid
                
                # Place the number at both positions
                arr[i] = arr[nextindex] = num
                used[num] = True

                if generateSub(i + 1):  # Recursive call
                    return True  # Found valid sequence
                
                # Backtrack
                arr[i] = arr[nextindex] = 0
                used[num] = False
            
            return False  # No valid sequence found
        
        generateSub(0)
        return arr