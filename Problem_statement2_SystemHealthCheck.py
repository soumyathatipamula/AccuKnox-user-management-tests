import psutil
import datetime

# Set limits
cpu_limit = 80
memory_limit = 80
disk_limit = 90

# Get system info
cpu = psutil.cpu_percent()
memory = psutil.virtual_memory().percent
disk = psutil.disk_usage('/').percent

# Create a log message
time_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
log = f"\n[{time_now}] CPU: {cpu}%, Memory: {memory}%, Disk: {disk}%"

# Print basic info
print(log)

# Save alerts if limits crossed
with open("simple_system_log.txt", "a") as file:
    if cpu > cpu_limit:
        file.write(f"{log} --> CPU usage too high!\n")
    if memory > memory_limit:
        file.write(f"{log} --> Memory usage too high!\n")
    if disk > disk_limit:
        file.write(f"{log} --> Disk usage too high!\n")
