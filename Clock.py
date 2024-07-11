from datetime import datetime, timedelta

class Clock:
    def __init__(self, start_time_str='8:00 AM'):
        self.current_time = datetime.strptime(start_time_str, '%I:%M %p')

    def addMinutes(self, minutes):
        self.current_time += timedelta(minutes=minutes)

    def getTime(self):
        return self.current_time