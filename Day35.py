import socket
from concurrent.futures import ThreadPoolExecutor

COMMON_PORTS = {
    20: "FTP Data",
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
    3389: "Remote Desktop",
    5432: "PostgreSQL",
    8080: "HTTP Alternate"
}

open_ports = []


def scan_port(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)

        result = sock.connect_ex((host, port))

        if result == 0:
            service = COMMON_PORTS.get(port, "Unknown Service")
            print(f"✅ Port {port} OPEN ({service})")
            open_ports.append((port, service))

        sock.close()

    except:
        pass


print("===== NETWORK PORT SCANNER =====")

host = input("Enter Host/IP (Example: 127.0.0.1): ")

print("\nScanning Common Ports...\n")

with ThreadPoolExecutor(max_workers=50) as executor:
    for port in COMMON_PORTS.keys():
        executor.submit(scan_port, host, port)

print("\n===== SCAN COMPLETE =====")

if open_ports:
    with open("port_scan_report.txt", "w") as report:

        report.write(f"Target: {host}\n\n")
        report.write("Open Ports\n")
        report.write("=" * 30 + "\n")

        for port, service in sorted(open_ports):
            report.write(f"{port} - {service}\n")

    print(f"Open Ports Found: {len(open_ports)}")
    print("✅ Report Saved as port_scan_report.txt")

else:
    print("No Common Open Ports Found.")
