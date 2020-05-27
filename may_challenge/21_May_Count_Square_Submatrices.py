"""
Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.



Example 1:

Input: matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
Output: 15
Explanation:
There are 10 squares of side 1.
There are 4 squares of side 2.
There is  1 square of side 3.
Total number of squares = 10 + 4 + 1 = 15.
Example 2:

Input: matrix =
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
Output: 7
Explanation:
There are 6 squares of side 1.
There is 1 square of side 2.
Total number of squares = 6 + 1 = 7.


Constraints:

1 <= arr.length <= 300
1 <= arr[0].length <= 300
0 <= arr[i][j] <= 1
"""


class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        self.mat = matrix
        result = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1:
                    result += 1

        for k in range(0, len(matrix)):
            for i in range(0, len(matrix) - k - 1):
                for j in range(0, len(matrix[0]) - k - 1):
                    p = i + k + 1
                    q = j + k + 1
                    if self.is_square(i, j, p, q):
                        result += 1

        return result

    def is_square(self, i, j, p, q):
        count = 0
        rows = p - i + 1
        cols = q - j + 1
        for l in range(i, p + 1):
            for m in range(j , q + 1):
                if self.mat[l][m] == 1:
                    count += 1

        if count == rows * cols:
            return True
        else:
            return False
