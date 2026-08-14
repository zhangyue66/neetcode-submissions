class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        column = len(matrix[0])

        # first identify which row using bs
        i,j = 0,row-1
        while i <= j:
            mid = (i+j) // 2
            if matrix[mid][-1] < target:
                i += 1
            elif matrix[mid][0] > target:
                j -= 1
            else:
                break

        if i > j:
            #the row we found is not there
            return False
        row = (i+j)//2

        l,r = 0, column-1
        while l<= r:
            mid = (l+r) //2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                r = mid-1
            else:
                l = mid+1
        return False

