import json
from pathlib import Path


class Reader:

    def read_lines(self) -> list[str]:
        raise Exception("not yet implemented")


class FileReader(Reader):

    def __init__(self, path: Path|str):
        self._path = Path(path)

    def read(self) -> str:
        return self._path.read_text('utf-8')

    def read_lines(self) -> list[str]:
        return [l for l in self.read().split('\n') if l.strip()]


class User:
    def __init__(self, name: str):
        self.name = name

    @classmethod
    def from_json(cls, blob) -> 'User' | None:
        if 'name' not in blob:
            return
        return cls(blob['name'])


class UserLoader:
    def __init__(self, reader: Reader):
        self._file_reader = reader

    def get_users(self) -> list[User]:
        ret = [User.from_json(json.loads(line)) for line in self._file_reader.read_lines()]
        return [r for r in ret if r is not None]
