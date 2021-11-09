import datetime


class TimeDesk:
    def __init__(self, second):
        self.second = second

    def secondsToText(self):
        days = self.second // 86400
        hours = (self.second - days * 86400) // 3600
        minutes = (self.second - days * 86400 - hours * 3600) // 60
        seconds = self.second - days * 86400 - hours * 3600 - minutes * 60
        result = ("{0} day{1}, ".format(days, "s" if days != 1 else "") if days else "") + \
                 ("{0} hour{1}, ".format(hours, "s" if hours != 1 else "") if hours else "") + \
                 ("{0} minute{1}, ".format(minutes, "s" if minutes != 1 else "") if minutes else "") + \
                 ("{0} second{1}, ".format(seconds, "s" if seconds != 1 else "") if seconds else "")
        return result

    def __str__(self):
        return f'Second: {self.second}'


time_1 = TimeDesk(second=86401)
print(time_1)
print(time_1.secondsToText())