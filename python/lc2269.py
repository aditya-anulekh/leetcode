class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        num_str = str(num)
        n = len(num_str)
        
        k_beauty = 0

        for i in range(n - k + 1):
            try:
                if num%int(num_str[i:i+k]) == 0:
                    k_beauty += 1
            except ZeroDivisionError:
                pass
        return k_beauty



if __name__ == "__main__":
    s = Solution()
    print(s.divisorSubstrings(430043, 2))
    print(s.divisorSubstrings(240, 2))
        