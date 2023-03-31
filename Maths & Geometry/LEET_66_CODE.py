def plusOne(self, digits: List[int]) -> List[int]:
        res = [0] * (len(digits) + 1)
        carry = 1
        for i in range(len(digits) - 1,-1,-1):
            res[i + 1] = digits[i] + carry
            if digits[i] + carry > 9:
                carry = 1
                res[i + 1] = 0
            else:
                carry = 0
        if carry == 1:
            res[0] += 1
        return res[1:] if res[0] == 0 else res