import requests
import datetime

# Set the URL to check
url = "https://example.com"  # Change this to the website you want to check

# Get the current time
time_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

try:
    response = requests.get(url)
    status_code = response.status_code

    if status_code == 200:
        message = f"[{time_now}] ✅ {url} is UP. Status: {status_code}"
    else:
        message = f"[{time_now}] ⚠️ {url} is reachable but returned status: {status_code}"

except Exception as e:
    message = f"[{time_now}] ❌ {url} is DOWN. Error: {str(e)}"

# Print and save the message
print(message)
with open("simple_app_log.txt", "a") as file:
    file.write(message + "\n")
