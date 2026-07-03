import cv2
from pyzbar.pyzbar import decode
import os

print("===== QR CODE SCANNER =====")

image_path = input("Enter QR Image Path: ")

if not os.path.exists(image_path):
    print("❌ Image Not Found!")
    exit()

image = cv2.imread(image_path)

qr_codes = decode(image)

if not qr_codes:
    print("❌ No QR Code Found!")

else:
    print(f"\n✅ {len(qr_codes)} QR Code(s) Detected\n")

    for index, qr in enumerate(qr_codes, start=1):

        data = qr.data.decode("utf-8")
        qr_type = qr.type

        print(f"QR Code {index}")
        print("-" * 30)
        print(f"Type : {qr_type}")
        print(f"Data : {data}")
        print()
