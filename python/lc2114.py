class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        return len(max(sentences, key=lambda x:len(x.split(" "))).split(" "))


if __name__ == "__main__":
    s = Solution()
    print(s.mostWordsFound(["alice and bob love leetcode", "i think so too", "this is great thanks very much"]))