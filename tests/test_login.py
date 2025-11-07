from pages.login_page import LoginPage
from playwright.sync_api import expect

def test_login_success(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("Admin", "admin123")

    # Wait and assert for successful login (presence of Admin tab)
    admin_tab = page.locator("a[href='/web/index.php/admin/viewAdminModule']")
    expect(admin_tab).to_be_visible(timeout=5000)

    print("✅ Login test passed.")
