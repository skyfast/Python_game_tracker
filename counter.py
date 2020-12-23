import datetime
class CounterBoi:
    def __init__(self, target, file, date):  # target is the points we need, file is where we read the start from
        self.target_count = target
        file = open(file, 'r')
        self.current_count = int(file.read())
        self.end_date = date

    def show_count(self):
        return self.current_count

    def show_target(self):
        return self.current_count

    def show_left(self):
        return self.target_count - self.current_count

    def take_a_win(self):
        self.current_count += 10

    def take_a_lose(self):
        self.current_count += 5

    def take_a_bonus(self, value):
        self.current_count += value

    def hard_reset(self, value):
        self.current_count = value

    def save(self, file):
        f = open(file, "w")
        f.write(str(self.current_count))

    def time_left(self):
        time_now = datetime.datetime.now()
        time_left = self.end_date - time_now
        return time_left.days
