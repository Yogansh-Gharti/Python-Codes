import csv
import socket
from concurrent.futures import ThreadPoolExecutor
from ping3 import ping

active_devices = []


def scan_ip(ip):
    try:
        response = ping(ip, timeout=1)

        if response is not None:
            try:
                hostname = socket.gethostbyaddr(ip)[0]
            except:
                hostname = "Unknown"

            print(f"✅ {ip} ({hostname})")

            active_devices.append([ip, hostname])

    except:
        pass


print("===== LOCAL NETWORK DEVICE SCANNER =====")

network = input(
    "Enter Network Prefix (Example: 192.168.1): "
)

print("\nScanning...\n")

with ThreadPoolExecutor(max_workers=100) as executor:

    for i in range(1, 255):
        ip = f"{network}.{i}"
        executor.submit(scan_ip, ip)

print("\n===== ACTIVE DEVICES =====")

if active_devices:

    for device in active_devices:
        print(f"{device[0]} - {device[1]}")

    with open(
        "network_scan_report.csv",
        "w",
        newline=""
    ) as file:

        writer = csv.writer(file)

        writer.writerow(["IP Address", "Hostname"])

        writer.writerows(active_devices)

    print(
        "\n✅ Report Saved as network_scan_report.csv"
    )

else:
    print("No Active Devices Found.")
