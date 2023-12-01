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


def verify_admin(user: User2 | User) -> bool:
    return isinstance(user, User2) and user.is_admin

def verify_regular_user(user: User2 | User) -> bool:
    return isinstance(user, User2) and user.is_admin is False


def get_admin(user_name: str) -> Admin | None:
    for user in users:
        if verify_admin(user) and user.name == user_name:
            return user


def get_old_user(user_name: str) -> User:
    for user in users:
        if isinstance(user, User) and user.name == user_name:
            return user


def get_regular_user(user_name: str) -> User2:
    for user in users:
        if verify_regular_user(user) and user.name == user_name:
            return user


def get_user(user_name: str,
             is_admin: bool = False,
             consider_old_users: bool = False) -> User | User2 | Admin | None:
    if is_admin:
        return get_admin(user_name)
    if consider_old_users:
        return get_old_user(user_name)
    return get_regular_user(user_name)


