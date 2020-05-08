"""
You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point.
Check if these points make a straight line in the XY plane.
"""


class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        x = coordinates[0][0]
        y = coordinates[0][1]

        if (coordinates[1][0] - coordinates[0][0]) == 0:
            x_intercept = coordinates[0][0]
            if len(coordinates) > 2:
                for i in range(2, len(coordinates)):
                    if coordinates[i][0] != x_intercept:
                        return False
                return True
            else:
                return True
        slope = (coordinates[1][1] - coordinates[0][1])/(coordinates[1][0] - coordinates[0][0])

        b = y - slope*x

        # Equation: y = mx+b

        if len(coordinates) > 2:
            for i in range(2, len(coordinates)):
                if coordinates[i][1] != slope*coordinates[i][0] + b:
                    return False
            return True
        else:
            return True
