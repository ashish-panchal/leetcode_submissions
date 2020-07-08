class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 0
        no_of_digits = len(digits)
        result = []

        while no_of_digits > 0:
            number = int(digits[no_of_digits - 1])

            if no_of_digits == len(digits):
                number += 1

            if carry != 0:
                number += carry
                carry = 0

            if number > 9:
                carry = int(str(number)[0])
                result.append(str(number)[1])

            else:
                result.append(str(number))

            no_of_digits -= 1

        if carry > 0:
            result.append(str(carry))

        final = result[::-1]
        return final
