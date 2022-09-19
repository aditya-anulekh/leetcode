class Solution:
    def numberOfMatches(self, n: int) -> int:
        matches = 1

        if n <= 1:
            return 0
        
        while n > 2:
            if n % 2 == 0:
                matches += n/2
                n = n / 2
            else:
                matches += (n - 1) / 2
                n = (n - 1) / 2 + 1

        return int(matches)
            


if __name__ == "__main__":
    s = Solution()
    print(s.numberOfMatches(7))
