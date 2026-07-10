import os
import requests
from tqdm import tqdm


def download_file(url):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()

        filename = url.split("/")[-1]

        if not filename:
            filename = "downloaded_file"

        total_size = int(response.headers.get("content-length", 0))
        block_size = 1024

        progress = tqdm(
            total=total_size,
            unit="B",
            unit_scale=True,
            desc=filename
        )

        with open(filename, "wb") as file:

            for data in response.iter_content(block_size):

                file.write(data)
                progress.update(len(data))

        progress.close()

        print(f"\n✅ Download Complete!")
        print(f"Saved As: {os.path.abspath(filename)}")

    except requests.exceptions.RequestException as e:
        print("❌ Download Failed!")
        print(e)


print("===== FILE DOWNLOADER =====")

url = input("Enter File URL: ")

download_file(url)
