def reverse(self, x: int) -> int:
        neg_val = True if x < 0 else False
        min_int = -2147483648
        max_int = 2147483647
        res = 0
        while(x != 0):
            digit = abs(x)%10
            x = int(x/10)
            if (res > int(max_int/10) or res == int(max_int/10) and digit > max_int%10):
                return 0
            if (res < int(min_int/10) or res == int(min_int/10) and digit < abs(max_int)%10):
                return 0
            res = res * 10 + digit
        return res * -1 if neg_val else res