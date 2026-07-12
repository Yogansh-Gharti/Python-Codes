import requests
import pyperclip
from datetime import datetime

HISTORY_FILE = "url_history.txt"


def shorten_url(long_url):
    api = f"https://tinyurl.com/api-create.php?url={long_url}"

    try:
        response = requests.get(api, timeout=10)

        if response.status_code == 200:

            short_url = response.text

            pyperclip.copy(short_url)

            print("\n===== SHORT URL =====")
            print(short_url)
            print("\n✅ Copied to Clipboard!")

            with open(HISTORY_FILE, "a") as file:

                file.write(
                    f"{datetime.now()}\n"
                )

                file.write(
                    f"Original : {long_url}\n"
                )

                file.write(
                    f"Short URL: {short_url}\n"
                )

                file.write("-" * 50 + "\n")

        else:
            print("Failed to shorten URL.")

    except Exception as e:
        print("❌ Error:", e)


print("===== URL SHORTENER =====")

url = input("Enter Long URL: ")

if not url.startswith("http"):
    url = "https://" + url

shorten_url(url)
