class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x:x[1],reverse=True)
        totalval=0
        for i,j in boxTypes:
            if i<truckSize:
                totalval+=i*j
                truckSize-=i
            else:
                totalval+=j*truckSize
                break
        return totalval
        