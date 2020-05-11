"""
An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to
65535).

Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value
newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting
pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with
the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the
newColor.

At the end, return the modified image.

Example 1:
Input:
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation:
From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected
by a path of the same color as the starting pixel are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected
to the starting pixel.
Note:

The length of image and image[0] will be in the range [1, 50].
The given starting pixel will satisfy 0 <= sr < image.length and 0 <= sc < image[0].length.
The value of each color in image[i][j] and newColor will be an integer in [0, 65535].
"""


class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        #self.image = image
        self.image = []


        for i in range(len(image)):
            self.image.append([])
            for j in range(len(image[i])):
                value = {"color": image[i][j], "visited": False}
                self.image[i].append(value)

        current_color = image[sr][sc]

        self.flood_all(image, sr, sc, current_color, newColor)

        for i in range(len(image)):
            for j in range(len(image[i])):
                image[i][j] = self.image[i][j]["color"]
        return image

    def flood_all(self, image, row, col, current_color, newColor):
        if row < 0 or row >= len(image) or col < 0 or col >= len(image[0]):
            return

        if image[row][col] != current_color:
            return
        elif image[row][col] == current_color and self.image[row][col]["visited"]:
            return
        elif image[row][col] == current_color and not self.image[row][col]["visited"]:
            self.image[row][col]["color"] = newColor
            self.image[row][col]["visited"] = True

        self.flood_all(image, row + 1, col, current_color, newColor)
        self.flood_all(image, row - 1, col, current_color, newColor)
        self.flood_all(image, row, col + 1, current_color, newColor)
        self.flood_all(image, row, col - 1, current_color, newColor)
