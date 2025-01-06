from datetime import timedelta
# clock tracks time in order to ensure packages are delivered on time
class Clock:
    def __init__(self, startTime):
        self.current_time = startTime

    def addMinutes(self, minutes):
        self.current_time += timedelta(minutes=minutes)

    def getTime(self):
        return self.current_time
