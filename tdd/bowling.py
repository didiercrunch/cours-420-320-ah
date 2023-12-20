
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
        return self.first_throw != 10 and self.score() >= 10

    def requires_extra_throw(self):
        if self.is_spare():
            return self.xtra_throw is None
        return False

    def set_extra_throw(self, throw):
        self.xtra_throw = throw

    def score(self):
        return ((self.first_throw or 0)
                + (self.second_throw or 0)
                + (self.xtra_throw or 0))


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


class BowlingGame2:
    def __init__(self):
        self.case = Case()

    def last_case(self):
        case = self.case
        while case.next is not None:
            case = case.next
        return case

    def add_case(self):
        self.last_case().set_next(Case())

    def throw(self, pins):
        if self.last_case().is_completed():
            self.add_case()
        self.last_case().throw(pins)

    def score(self):
        ret = 0
        case = self.case
        while case is not None:
            ret += case.score()
            case = case.next
        return ret;


class Case:
    def __init__(self):
        self.next = None
        self.first_throw = None
        self.second_throw = None

    def throw(self, pin):
        if self.first_throw is None:
            self.first_throw = pin
        else:
            self.second_throw = pin

    def set_next(self, case):
        self.next = case

    def extra_score(self):
        if self.next is None:
            return 0
        if self.is_spare():
            return self.next.first_throw or 0
        return 0

    def is_completed(self):
        if self.first_throw == 10:
            return True
        return (self.first_throw is not None
                and self.second_throw is not None)

    def is_spare(self):
        return self.raw_score() == 10 and not self.is_strike()

    def is_strike(self):
        return self.raw_score() == 10

    def raw_score(self):
        return ((self.first_throw or 0)
                + (self.first_throw or 0))

    def score(self):
        return self.raw_score() + self.extra_score()

