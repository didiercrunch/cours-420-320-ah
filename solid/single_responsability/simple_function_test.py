from solid.single_responsability.simple_function import get_user


class TestGetUser:
    def test_happy_path(self):
        assert get_user("marie-eve") is None
        assert get_user("walid").name == 'walid'

    def test_admin(self):
        assert get_user("tristan") is None
        assert get_user("tristan", is_admin=True) is not None
        assert get_user("tristan", is_admin=True).name == "tristan"

    def test_old_users(self):
        assert get_user("jonathan") is None
        assert get_user("jonathan", is_admin=True) is None
        assert get_user("jonathan", consider_old_users=True) is not None
        assert get_user("jonathan", consider_old_users=True).name == "jonathan"
