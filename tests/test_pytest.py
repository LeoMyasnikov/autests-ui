class TestUserLogin:
    def test_login(self):
        print('Hello!')

    def test_login_two(self):
        print('Guys!')

    def test_assert_positive(self):
        assert (2+2) == 4

    def test_assert_negative(self):
        four = (2+2)
        assert four == 5, "4 != 5"
