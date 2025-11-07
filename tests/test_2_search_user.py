from pages.admin_page import AdminPage

def test_search_user(page_setup):
    page = page_setup
    admin = AdminPage(page)

    admin.go_to_admin()
    with open("user_info.txt") as f:
        username = f.read().strip()

    admin.search_user(username)
    row = admin.get_user_row_by_username(username)
    assert row.is_visible(), f"❌ User {username} not found."
    print(f"🔍 User '{username}' found successfully.")
