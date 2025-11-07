# OrangeHRM Admin Module Automation (Playwright + Python)

This project contains automated end-to-end tests for the Admin User Management module of the OrangeHRM demo site.

The tests are written in **Python** using **Playwright** and **Pytest**. They follow the Page Object Model (POM) design pattern.

##  scenarios Covered

The test suite covers the full life cycle of a user:

* **Login:** The test logs in as an Admin user.
* **Add User:** Creates a new user with a unique username.
* **Search User:** Searches for the newly created user to verify it exists.
* **Edit User:** Edits the user's role and status.
* **Validate Update:** Searches for the user again to validate that the changes were saved.
* **Delete User:** Deletes the user to clean up the environment.

## Project Setup

1.  **Clone the repository:**
    ```bash
    git clone <your-repository-url>
    cd AccuKnox-user-management-tests
    ```

2.  **Create and activate a virtual environment:**

    * **On macOS/Linux:**
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```

    * **On Windows:**
        ```bash
        python -m venv venv
        .\venv\Scripts\activate
        ```

3.  **Install dependencies:**
    Install all the required Python packages from the `requirements.txt` file.
    ```bash
    pip install -r requirements.txt
    ```

4.  **Install Playwright browsers:**
    This one-time command downloads the browsers (Chromium, Firefox, WebKit) needed for Playwright.
    ```bash
    playwright install
    ```

## How to Run the Test Cases

All tests are managed and run using `pytest`.

To run the full test suite in order (Add -> Search -> Edit -> Validate -> Delete), simply run the following command in your terminal:

```bash
pytest -s -v