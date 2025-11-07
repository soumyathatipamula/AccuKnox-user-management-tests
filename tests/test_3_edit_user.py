from pages.admin_page import AdminPage

def test_edit_user(page_setup):
    page = page_setup
    admin = AdminPage(page)

    admin.go_to_admin()
    with open("user_info.txt") as f:
        username = f.read().strip()

    updated_role, updated_status = admin.edit_user(username, "ESS", "Disabled")
    print(f"Updated Role: {updated_role}")
    print(f"Updated Status: {updated_status}")

