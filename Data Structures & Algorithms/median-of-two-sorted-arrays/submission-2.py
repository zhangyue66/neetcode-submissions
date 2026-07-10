class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A,B = nums1,nums2
        
        if len(A) > len(B):
            A,B = B,A
        m,n=len(A),len(B)
        

        # always start on shorter list first
        
        la,ra=0,m-1
        while True:
            mid_a = (la+ra)//2
            mid_total = (m+n) //2
            mid_b = mid_total-mid_a -2 # why -2 is needed

            print(f'A is {A},b is {B}')
            print(mid_a,mid_b)
            Aleft = A[mid_a] if mid_a >= 0 else float("-infinity")
            Aright = A[mid_a+1] if (mid_a + 1) < len(A) else float("infinity")
            Bleft = B[mid_b] if mid_b >= 0 else float("-infinity")
            Bright = B[mid_b+1] if (mid_b + 1) < len(B) else float("infinity")

            if Aleft <= Bright and Bleft <= Aright:
                if (m+n) % 2 == 1:
                    return min(Aright,Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                ra = mid_a-1
            else:
                la = mid_a + 1