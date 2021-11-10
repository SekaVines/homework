class TimeDesk:
    def __init__(self, second):
        self.second = second


def SecondConverter(x):
    d = int(x / 86400)
    x -= (d * 86400)
    h = int(x / 3600)
    x -= (h * 3600)
    m = int(x / 60)
    x -= (m * 60)
    s = x
    print("Your input is equal to ", d, " days, ", h, " hours, ", m, " minutes, and ", s, "seconds.")


SecondConverter(int(input("Your number:")))
