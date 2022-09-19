class Solution(object):
    def twoOutOfThree(self, nums1, nums2, nums3):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :rtype: List[int]
        """
        # all_vals = set([*nums1, *nums2, *nums3])

        all_vals = []
        all_vals.extend(nums1)
        all_vals.extend(nums2)
        all_vals.extend(nums3)
        all_vals = set(all_vals)

        return [i for i in all_vals if sum([i in nums1, i in nums2, i in nums3]) >= 2]


if __name__ == "__main__":
    s = Solution()
    print(s.twoOutOfThree(nums1 = [1,1,3,2], nums2 = [2,3], nums3 = [3]))