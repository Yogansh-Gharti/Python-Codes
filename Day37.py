import requests
import time
from datetime import datetime


def check_website(url):
    try:
        start_time = time.time()

        response = requests.get(url, timeout=10)

        end_time = time.time()

        response_time = (end_time - start_time) * 1000

        report = f"""
========== WEBSITE STATUS REPORT ==========

Date & Time   : {datetime.now().strftime("%d-%m-%Y %H:%M:%S")}

Website       : {url}
Status Code   : {response.status_code}
Status        : ONLINE
Response Time : {response_time:.2f} ms

Server        : {response.headers.get('Server', 'Unknown')}
Content Type  : {response.headers.get('Content-Type', 'Unknown')}

===========================================
"""

        print(report)

        with open("website_log.txt", "a") as file:
            file.write(report)
            file.write("\n")

        print("✅ Report Saved Successfully!")

    except requests.exceptions.RequestException as e:

        print("\n❌ Website is Offline or Unreachable!")

        with open("website_log.txt", "a") as file:
            file.write(
                f"{datetime.now()} | {url} | OFFLINE\n"
            )

        print(e)


print("===== WEBSITE STATUS CHECKER =====")

website = input("Enter Website URL: ")

if not website.startswith("http"):
    website = "https://" + website

check_website(website)
