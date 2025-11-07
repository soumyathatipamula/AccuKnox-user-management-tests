from pages.admin_page import AdminPage

def test_delete_user(page_setup):
    page = page_setup
    admin = AdminPage(page)

    admin.go_to_admin()
    with open("user_info.txt") as f:
        username = f.read().strip()

    admin.delete_user(username)
    print(f"🗑️ User '{username}' deleted successfully.")
