import pytest


@pytest.mark.smoke
def test_smoke_case():
    ...


@pytest.mark.regression
def test_regression_case():
    ...


@pytest.mark.smoke
class TestSuit:
    def test_case1(self):
        ...

    def test_case2(self):
        ...


@pytest.mark.regression
class TestUserAuthentication:
    @pytest.mark.smoke
    def test_login(self):
        ...

    @pytest.mark.slow
    def test_password_reset(self):
        ...

    def test_logout(self):
        ...


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.critical
def test_critical_login():
    ...


@pytest.mark.ui
class TestUserInterface:

    @pytest.mark.smoke
    @pytest.mark.critical
    def test_login_button(self):
        pass

    @pytest.mark.regression
    def test_forgot_password_link(self):
        pass

    @pytest.mark.smoke
    def test_signup_form(self):
        pass


@pytest.mark.performance
def test_memory_usage():
    pass

@pytest.mark.slow
class TestStress:
    def test_stress_1(self):
        pass

    @pytest.mark.performance
    def test_stress_2(self):
        pass


@pytest.mark.smoke
def test_user_exists():
    pass


@pytest.mark.regression
class TestUserFlow:
    @pytest.mark.smoke
    def test_user_can_login(self):
        pass

    def test_user_can_register(self):
        pass