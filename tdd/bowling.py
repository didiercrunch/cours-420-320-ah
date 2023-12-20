
class BowlingCase:
    def __init__(self):
        self.first_throw = None
        self.second_throw = None
        self.xtra_throw = None

    def add_score(self, pins_down):
        if self.first_throw is None:
            self.first_throw = pins_down
        else:
            self.second_throw = pins_down

    def is_completed(self):
        if self.first_throw == 10:
            return True
        return isinstance(self.first_throw, int) and isinstance(self.second_throw, int)

    def is_spare(self):
        return self.first_throw != 10 and self.score() == 10

    def requires_extra_throw(self):
        if self.is_spare():
            return self.xtra_throw is None
        return False

    def set_extra_throw(self, throw):
        self.xtra_throw = throw

    def score(self):
        return (self.first_throw or 0) + (self.second_throw or 0)


class BowlingGame:
    def __init__(self):
        self._score = [BowlingCase() for i in range(10)]

    def throw(self, pin_downs):
        for case in self._score:
            if not case.is_completed():
                case.add_score(pin_downs)
                return

    def score(self):
        return sum([case.score() for case in self._score])
