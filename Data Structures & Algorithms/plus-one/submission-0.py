class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        ans = []
        n = len(digits)
        
        for i in range(n-1,-1,-1):
            if carry:
                num = digits[i] + carry
                carry = num // 10
                new_num = num % 10
                print(f"{num} {carry} {new_num}")

                ans.append(new_num)
            else:
                ans.append(digits[i])

        if carry:
            ans.append(carry)
        return ans[::-1]