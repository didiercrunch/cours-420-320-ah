from solid.open_close.users import UserStorage, User, SQliteUserStorage


class TestUserStorage:
    def test_happy_path(self):
        storage = UserStorage()
        storage.save(User('Eliotte'))
        assert storage.get('Eliotte') is not None

    def test_not_found(self):
        storage = UserStorage()
        assert storage.get('Eliotte') is None

    def test_get_if_name_starts_by_a(self):
        storage = UserStorage()
        storage.save(User('Eliotte'))
        storage.save(User('Andre'))

        assert storage.get_if_name_starts_by_a('Eliotte') is None
        assert storage.get_if_name_starts_by_a('Andre') is not None


class TestSQliteUserStorage:
    def test_happy_path(self):
        storage = SQliteUserStorage.create(":memory:")
        storage.save(User('Eliotte'))
        assert storage.get('Eliotte') is not None

    def test_not_found(self):
        storage = SQliteUserStorage.create(":memory:")
        assert storage.get('Eliotte') is None

    def test_get_if_name_starts_by_a(self):
        storage = SQliteUserStorage.create(":memory:")
        storage.save(User('Eliotte'))
        storage.save(User('Andre'))

        assert storage.get_if_name_starts_by_a('Eliotte') is None
        assert storage.get_if_name_starts_by_a('Andre') is not None

