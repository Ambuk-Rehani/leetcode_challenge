def myPow(self, x: float, n: int) -> float:
        def poww(x,n):
            if x == 0:
                return 0
            if n == 0:
                return 1
            val = poww(x,n//2)
            if (n % 2 == 0):
                return val * val
            else:
                return val * val * x
        res = poww(x,abs(n))
        return res if n>=0 else 1/res