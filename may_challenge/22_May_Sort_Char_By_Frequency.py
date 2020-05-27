"""
Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
"""


class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        hash_map = {}

        for char in range(len(s)):
            if s[char] not in hash_map:
                hash_map[s[char]] = 1
            else:
                hash_map[s[char]] += 1

        # {k: v for k, v in sorted(hash_map.items(), key=lambda item: item[1])}
        sorted_x = sorted(hash_map.items(), key=lambda kv: kv[1])
        sorted_x.reverse()
        result = ""

        for char in sorted_x:
            length = char[1]
            for i in range(length):
                result += char[0]

        return result
