import os
import platform
import socket
import psutil


def bytes_to_gb(size):
    return round(size / (1024 ** 3), 2)


print("===== SYSTEM INFORMATION TOOL =====\n")

system = platform.system()
release = platform.release()
version = platform.version()
machine = platform.machine()
processor = platform.processor()
python_version = platform.python_version()
hostname = socket.gethostname()

try:
    ip_address = socket.gethostbyname(hostname)
except:
    ip_address = "Unavailable"

ram = psutil.virtual_memory()

disk = psutil.disk_usage('/')

cpu_usage = psutil.cpu_percent(interval=1)

report = f"""
========== SYSTEM REPORT ==========

Operating System : {system}
OS Release       : {release}
OS Version       : {version}

Machine Type     : {machine}
Processor        : {processor}

Python Version   : {python_version}

Host Name        : {hostname}
IP Address       : {ip_address}

CPU Usage        : {cpu_usage} %

RAM Total        : {bytes_to_gb(ram.total)} GB
RAM Used         : {bytes_to_gb(ram.used)} GB
RAM Available    : {bytes_to_gb(ram.available)} GB

Disk Total       : {bytes_to_gb(disk.total)} GB
Disk Used        : {bytes_to_gb(disk.used)} GB
Disk Free        : {bytes_to_gb(disk.free)} GB

===================================
"""

print(report)

with open("system_report.txt", "w") as file:
    file.write(report)

print("✅ Report Saved as system_report.txt")
