from datetime import datetime


class User:
    def __init__(self, name: str, password: str):
        self.name = name
        self._password = password

    def is_right_password(self, password) -> bool:
        # ne JAMAIS faire cela
        return password == self._password


class Admin(User):
    def __init__(self, name: str, password: str, one_time_password: str):
        super(name, password)
        self._one_time_password = one_time_password

    def is_right_password(self, password, otp_challange) -> bool:
        is_otp_valid = self._one_time_password == otp_challange
        return super().is_right_password(password) and is_otp_valid


class LoggedInUser:
    def __init__(self, user: User, logged_in_time: datetime):
        self.user = user
        self.logged_in_time = logged_in_time


def loging(user: User, password: str) -> LoggedInUser | None:
    if not user.is_right_password(password):
        return None

    return LoggedInUser(user, datetime.utcnow())