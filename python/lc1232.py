class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        if len(coordinates) <= 2:
            return True

        try:
            slope = (coordinates[1][1] - coordinates[0][1])/(coordinates[1][0] - coordinates[0][0])
            for point in coordinates[2:]:
                if point[1] - coordinates[0][1] != slope*(point[0] - coordinates[0][0]):
                    return False
        except ZeroDivisionError:
            for point in coordinates[2:]:
                if point[0] != coordinates[0][0]:
                    return False

        return True


if __name__ == "__main__":
    s = Solution()
    print(s.checkStraightLine([[2,1],[4,2],[6,3]]))