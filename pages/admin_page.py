from playwright.sync_api import expect

class AdminPage:
    def __init__(self, page):
        self.page = page

    def go_to_admin(self):
        self.page.locator("a:has-text('Admin')").click()
        expect(self.page.get_by_role("heading", name="System Users")).to_be_visible()

    def add_user(self, employee_name, username, password):
        self.page.locator("button:has-text('Add')").click()

    # Select User Role
        self.page.locator("div.oxd-select-wrapper").nth(0).click()
        self.page.locator("div[role='option']:has-text('Admin')").click()

    # Fill Employee Name and wait for dropdown options
        self.page.get_by_placeholder("Type for hints...").fill(employee_name)
        self.page.wait_for_selector(f"div[role='option']:has-text('{employee_name}')", timeout=5000)
        self.page.locator(f"div[role='option']:has-text('{employee_name}')").click()

    # Fill Username
        self.page.locator("input[autocomplete='off']").nth(0).fill(username)

    # Select Status
        self.page.locator("div.oxd-select-wrapper").nth(1).click()
        self.page.locator("div[role='option']:has-text('Enabled')").click()

    # Fill Password and Confirm
        self.page.locator("input[type='password']").nth(0).fill(password)
        self.page.locator("input[type='password']").nth(1).fill(password)

    # Click Save
        self.page.locator("button:has-text('Save')").click()

    # Wait for return to user list
        self.page.wait_for_selector("div.orangehrm-container", timeout=10000)
        expect(self.page.locator("div.orangehrm-container")).to_be_visible()

    def search_user(self, username):
        username_input = self.page.locator("//label[text()='Username']/../following-sibling::div//input")
        username_input.fill(username)
        self.page.locator("button:has-text('Search')").click()
        self.page.wait_for_selector(f"div.oxd-table-row:has-text('{username}')", timeout=5000)

    def get_user_row_by_username(self, username):
        return self.page.locator(f"div.oxd-table-row:has-text('{username}')")

    def edit_user(self, username, new_role, new_status):
        self.search_user(username)
        row = self.get_user_row_by_username(username)
        row.locator("i.bi-pencil-fill").click()  # Edit icon

    # Change role
        self.page.locator("div.oxd-select-wrapper").nth(0).click()
        self.page.locator(f"div[role='option']:has-text('{new_role}')").click()

    # Change status
        self.page.locator("div.oxd-select-wrapper").nth(1).click()
        self.page.locator(f"div[role='option']:has-text('{new_status}')").click()

    # Save the changes
        self.page.locator("button:has-text('Save')").click()

    # Wait for the changes to reflect
        self.page.wait_for_timeout(1500)

    # Re-search and return updated values
        self.search_user(username)
        row = self.get_user_row_by_username(username)
        updated_role = row.locator("div:nth-child(3)").inner_text()
        updated_status = row.locator("div:nth-child(5)").inner_text()
        return updated_role, updated_status

    def delete_user(self, username):
        self.search_user(username)
        self.page.locator(f"div.oxd-table-row:has-text('{username}') i.bi-trash").click()
        self.page.locator("button:has-text('Yes, Delete')").click()
        expect(self.page.locator("div.oxd-toast")).to_be_visible()
