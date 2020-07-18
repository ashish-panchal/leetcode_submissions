class Solution(object):
    def angleClock(self, hour, minutes):
        """
        :type hour: int
        :type minutes: int
        :rtype: float
        """
        hour_hand = 30 * hour + 0.5 * minutes
        minute_hand = 6 * minutes

        pos_diff = abs(hour_hand - minute_hand)

        if pos_diff < 180:
            return pos_diff
        else:
            return 360 - pos_diff