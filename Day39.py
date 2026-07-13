import hashlib
import requests


def check_password(password):
    sha1_hash = hashlib.sha1(
        password.encode()
    ).hexdigest().upper()

    prefix = sha1_hash[:5]
    suffix = sha1_hash[5:]

    url = f"https://api.pwnedpasswords.com/range/{prefix}"

    try:
        response = requests.get(url, timeout=10)

        if response.status_code != 200:
            print("Error connecting to API.")
            return

        hashes = response.text.splitlines()

        for line in hashes:
            hash_suffix, count = line.split(":")

            if hash_suffix == suffix:
                print("\n❌ Password Found in Data Breaches!")
                print(f"Times Leaked: {count}")
                return

        print("\n✅ Good News!")
        print("Password Not Found in Known Data Breaches.")

    except Exception as e:
        print("Error:", e)


print("===== PASSWORD LEAK CHECKER =====")

password = input("Enter Password: ")

check_password(password)
