class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()

        n = len(nums)

        if n == 0: return 0
        
        longest_streak = 1
        current_streak = 1

        for i in range(n - 1):
            if nums[i+1] == nums[i] + 1:
                current_streak += 1
            else:
                if current_streak > longest_streak:
                    longest_streak = current_streak
                current_streak = 1
        
        return max([longest_streak, current_streak])


if __name__ == "__main__":
    s = Solution()
    print(s.longestConsecutive([1,2,0,1]))
