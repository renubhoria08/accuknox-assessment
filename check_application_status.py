import requests
from datetime import datetime
import time

url = "https://google.com"

# Interval in seconds
check_interval = 60

# Number of retries to attempt
retry_count = 3

def check_application_status(url):
    for attempt in range(retry_count):
        try:
            start_time = time.time()
            response = requests.get(url)
            response_time = time.time() - start_time
            status_code = response.status_code
            if 200 <= status_code < 300:
                return "up", status_code, response_time
            else:
                time.sleep(1)
        except requests.exceptions.RequestException:
            time.sleep(1)
    return "down", None, None


def log_status(status, status_code, response_time):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    response_time_ms = (
        f"{response_time * 1000:.2f} ms" if response_time else "N/A"
    )
    log_entry = (
        f"[{current_time}] Application is {status}. "
        f"Status code: {status_code if status_code else 'N/A'}. "
        f"Response time: {response_time_ms}"
    )
    print(log_entry)


if __name__ == "__main__":
    while True:
        status, status_code, response_time = check_application_status(url)
        log_status(status, status_code, response_time)
        time.sleep(check_interval)
