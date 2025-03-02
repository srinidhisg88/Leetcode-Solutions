class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        merged_dict={}
        for id_,val in nums1:
            merged_dict[id_]=merged_dict.get(id_,0)+val
        for id_,val in nums2:
            merged_dict[id_]=merged_dict.get(id_,0)+val
        return sorted(merged_dict.items())