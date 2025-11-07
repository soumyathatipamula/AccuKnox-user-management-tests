from pages.admin_page import AdminPage

def test_validate_updated_user(page_setup):
    page = page_setup
    admin = AdminPage(page)

    admin.go_to_admin()
    with open("user_info.txt") as f:
        username = f.read().strip()

    admin.search_user(username)
    row = admin.get_user_row_by_username(username)
    role_text = row.locator("div:nth-child(3)").inner_text()
    status_text = row.locator("div:nth-child(5)").inner_text()

    assert role_text == "ESS", f"❌ Expected role 'ESS', found '{role_text}'"
    assert status_text == "Disabled", f"❌ Expected status 'Disabled', found '{status_text}'"

    print(f"✅ User '{username}' validated: Role = {role_text}, Status = {status_text}")
