from solid.single_responsability.simple_function import get_user, get_admin, get_old_user, get_regular_user


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




class TestRefactoredGetUser:
    def test_happy_path(self):
        assert get_regular_user("marie-eve") is None
        assert get_regular_user("walid").name == 'walid'

    def test_admin(self):
        assert get_admin("walid") is None
        assert get_admin("tristan") is not None
        assert get_admin("tristan").name == "tristan"

    def test_old_users(self):
        assert get_old_user("didier") is None
        assert get_old_user("jonathan") is not None
        assert get_old_user("jonathan").name == "jonathan"
