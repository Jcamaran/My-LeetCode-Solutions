class Solution(object):
    def findDifference(self, nums1, nums2):
        if nums1 == nums2:
            return [[],[]] 
        diff1 = set(nums1) - set(nums2)
        diff2 = set(nums2) - set(nums1)

        return [list(diff1), list(diff2)]
        
