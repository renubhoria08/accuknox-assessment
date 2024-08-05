import logging
import time

import psutil


logging.basicConfig(
    filename="system_health.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
)

# In percentage
CPU_THRESHOLD = 80
# In percentage
MEMORY_THRESHOLD = 80
# In percentage
DISK_THRESHOLD = 80

# Number of processes
PROCESS_THRESHOLD = 300


def check_cpu():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        logging.info(f"High CPU usage detected: {cpu_usage}%")
    return cpu_usage


def check_memory():
    memory_info = psutil.virtual_memory()
    memory_usage = memory_info.percent
    if memory_usage > MEMORY_THRESHOLD:
        logging.info(f"High Memory usage detected: {memory_usage}%")
    return memory_usage


def check_disk():
    disk_info = psutil.disk_usage("/")
    disk_usage = disk_info.percent
    if disk_usage > DISK_THRESHOLD:
        logging.info(f"Low Disk space detected: {disk_usage}% used")
    return disk_usage


def check_processes():
    process_count = len(psutil.pids())
    if process_count > PROCESS_THRESHOLD:
        logging.info(f"High number of processes detected: {process_count}")
    return process_count


def main():
    while True:
        cpu_usage = check_cpu()
        memory_usage = check_memory()
        disk_usage = check_disk()
        process_count = check_processes()

        print(f"CPU Usage: {cpu_usage}%")
        print(f"Memory Usage: {memory_usage}%")
        print(f"Disk Usage: {disk_usage}%")
        print(f"Number of Processes: {process_count}")

        time.sleep(5)


if __name__ == "__main__":
    main()
