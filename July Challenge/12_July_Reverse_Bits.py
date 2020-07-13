class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        formatted = format(n, 'b').zfill(32)
        
        result = int(formatted[::-1], 2)

        return result
