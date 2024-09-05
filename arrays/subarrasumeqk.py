class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # cnt=0
        # n=len(nums)
        # for i in range(n):
        #     sum=0
        #     for j in range(i,n):
        #         sum+=nums[j]
        #         if sum==k:
        #             cnt+=1
        # return cnt
        ## using prefix sum
        cnt=0
        presum=0
        map=defaultdict(int)
        map[0]=1
        n=len(nums)
        for i in range(n):
            presum+=nums[i]
            remove=presum-k
            cnt+=map[remove]
            map[presum]+=1
        return cnt
