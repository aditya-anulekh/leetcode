class Solution:
    def countPoints(self, rings: str) -> int:
        n = len(rings)

        counter = {i:[] for i in range(10)}

        for i in range(0, n, 2):
            color = rings[i]
            counter[int(rings[i+1])].append(color)

        return len([i for i in counter.values() if len(set(i)) == 3])


if __name__ == "__main__":
    s = Solution()
    print(s.countPoints("B0B6G0R6R0R6G9"))