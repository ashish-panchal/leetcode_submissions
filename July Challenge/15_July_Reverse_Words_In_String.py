class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split(" ")

        count = len(words)
        result = ""

        while count != 0:
            if words[count - 1] != "":
                if result != "":
                    result += " "

                result += words[count - 1]

            count -= 1

        return result