def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        count = 0
        dp_count = 0
        for i in range(1,n + 1):
            if (pow(2,count) == i):
                dp_count = 0
                count += 1
            dp[i] = dp[dp_count] + 1
            dp_count += 1
        return dp
