def check_fair(arr, arr_sum):
    evensum = sum([arr[i] for i in range(len(arr)) if i%2 == 0])
    return evensum == (arr_sum - evensum)


class Solution(object):
    def waysToMakeFair(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_ways = 0
        total = sum(nums)
        n = len(nums)
        for i in range(n):
            if check_fair(nums[:i] + nums[i+1:], total-nums[i]): num_ways += 1
        return num_ways
        