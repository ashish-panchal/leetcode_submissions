"""
There are 2N people a company is planning to interview. The cost of flying the i-th person to city A is costs[i][0], and the cost of flying the i-th person to city B is costs[i][1].

Return the minimum cost to fly every person to a city such that exactly N people arrive in each city.



Example 1:

Input: [[10,20],[30,200],[400,50],[30,20]]
Output: 110
Explanation:
The first person goes to city A for a cost of 10.
The second person goes to city A for a cost of 30.
The third person goes to city B for a cost of 50.
The fourth person goes to city B for a cost of 20.

The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.


Note:

1 <= costs.length <= 100
It is guaranteed that costs.length is even.
1 <= costs[i][0], costs[i][1] <= 1000
"""

class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        diff_dict = {}

        for i in range(len(costs)):
            diff_dict[str(i)] = abs(costs[i][0]-costs[i][1])

        sorted_x = sorted(diff_dict.items(), key = lambda kv: kv[1])
        sorted_x.reverse()
        num = len(costs)/2
        count_a = num
        count_b = num
        result = 0

        for k in sorted_x:
            index = int(k[0])

            if costs[index][0] < costs[index][1]:
                if count_a != 0:
                    result += costs[index][0]
                    count_a -= 1
                else:
                    result += costs[index][1]
                    count_b -=1
            elif costs[index][0] > costs[index][1]:
                if count_b != 0:
                    result += costs[index][1]
                    count_b -= 1
                else:
                    result += costs[index][0]
                    count_a -=1
            else:
                if count_b != 0:
                    result += costs[index][1]
                    count_b -= 1
                else:
                    result += costs[index][0]
                    count_a -=1
        return result