# https://leetcode.com/explore/featured/card/july-leetcoding-challenge/545/week-2-july-8th-july-14th/3390/
def angleClock(self, hour: int, minutes: int) -> float:
        hour%=12

        hour_delta_hour = 360/12
        minute_delta_minute = 360/60
        hour_delta_per_minute = 30/60

        hour_movement = hour*hour_delta_hour + minutes*hour_delta_per_minute

        minute_movement =  minutes*minute_delta_minute
        angle  = min(abs(hour_movement-minute_movement),360-abs(hour_movement-minute_movement))
        return angle
