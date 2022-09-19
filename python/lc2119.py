def reverse_num(num):
    digits = []
    while num > 0:
        digits.append(num%10)
        num = num//10
    if len(digits) == 0:
        digits = [0]
    return int(''.join(map(str, digits)))
    


class Solution(object):
    def isSameAfterReversals(self, num):
        """
        :type num: int
        :rtype: bool
        """
        reversed1 = reverse_num(num)
        return reverse_num(reversed1) == num


if __name__ == "__main__":
    s = Solution()
    print(s.isSameAfterReversals(0))
        