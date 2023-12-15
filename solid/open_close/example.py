class User:

    def __init__(self, email, company):
        self.email = email
        self.company = company

    def get_user_id(self) -> str:
        return self.email + "/" + self.company


class MockUser(User):

    def get_user_id(self) -> str:
        return self.email

    def get_real_name(self):
        return "andre"


def pretty_print_user(user: User):
    email, company = user.get_user_id().split("/")

