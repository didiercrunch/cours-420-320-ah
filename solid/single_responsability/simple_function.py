class User:
    def __init__(self, name):
        self.name = name
        self.isAdmin = False


class User2:
    def __init__(self, name):
        self.name = name
        self.is_admin = False


class Admin(User2):
    def __init__(self, name):
        super().__init__(name)
        self.is_admin = True


users = [
    User2('walid'),
    User2('haikel'),
    User2('manel'),
    Admin('tristan'),
    Admin('didier'),
    User('jonathan'),
    User('samuel'),
]


def get_user(user_name: str, is_admin: bool = False, consider_old_users: bool=False) -> User | User2 | Admin | None:
    for user in users:
        if user_name == user.name:
            if isinstance(user, User) and not consider_old_users:
                continue
            if isinstance(user, User2) and user.is_admin and not is_admin:
                continue
            return user
