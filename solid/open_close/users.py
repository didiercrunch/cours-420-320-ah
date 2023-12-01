import sqlite3


class User:
    def __init__(self, name: str):
        self.name = name


class UserStorage:
    def __init__(self):
        self._memory: list[User] = []

    def save(self, user: User) -> None:
        self._memory.append(user)

    def get(self, name: str) -> User | None:
        for user in self._memory:
            if user.name == name:
                return user

    def get_if_name_starts_by_a(self, name: str) -> User | None:
        if name.lower().startswith('a'):
            return self.get(name)


class SQliteUserStorage(UserStorage):
    def __init__(self, conn: sqlite3.Connection):
        self._conn = conn

    @classmethod
    def create(cls, url: str) -> 'SQliteUserStorage':
        conn = sqlite3.connect(url)
        conn.execute('''CREATE TABLE IF NOT EXISTS users(name TEXT UNIQUE NOT NULL)''')
        return cls(conn)

    def save(self, user: User) -> None:
        self._conn.execute(
            '''INSERT INTO users(name) VALUES (?)''', (user.name, )
        )

    def get(self, name: str) -> User | None:
        res = self._conn.execute("""SELECT name FROM users WHERE name = ?""", (name, )).fetchone()
        if res is None:
            return None
        return User(res[0])
