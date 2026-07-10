class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1,l2=0,0
        m,n=len(nums1),len(nums2)
        combi = []
        while l1 <= m-1 and l2 <= n-1:
            print(l1,l2)
            if nums1[l1] <= nums2[l2]:
                combi.append(nums1[l1])
                l1 += 1
            else:
                combi.append(nums2[l2])
                l2 += 1

        if l1<m:
            combi += nums1[l1:]
        if l2<n:
            combi += nums2[l2:]

        mid = (m+n)//2
        print(combi)
        if (m+n) % 2 == 0:
            return (combi[mid] + combi[mid-1])/2
        return combi[mid]