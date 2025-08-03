class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap={}
        st=[]
        ans=[]
        for n in reversed(nums2):
            while st and n>=st[-1]:
                st.pop()
            if st:
                hashmap[n]=st[-1]
            else:
                hashmap[n]=-1
            st.append(n)
        for n in nums1:
            ans.append(hashmap[n])
        return ans
        