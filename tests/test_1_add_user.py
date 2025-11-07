import time
from pages.admin_page import AdminPage

def test_add_user(page_setup):
    page = page_setup
    admin = AdminPage(page)

    admin.go_to_admin()
    username = f"testuser_{int(time.time())}"
    password = "testtest1"
    admin.add_user("John A Doe", username, password)

    with open("user_info.txt", "w") as f:
        f.write(username)

    print(f"✅ User '{username}' created and saved.")


