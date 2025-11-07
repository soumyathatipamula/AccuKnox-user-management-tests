import pytest

@pytest.fixture(scope="function")
def page_setup(page):
    # login flow
    from pages.login_page import LoginPage
    login = LoginPage(page)
    login.navigate()
    login.login("Admin", "admin123")
    return page
