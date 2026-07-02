import qrcode

print("===== QR CODE GENERATOR =====")

data = input("Enter Text / URL / Wi-Fi Info: ")
filename = input("Enter Output File Name: ")

if not filename.endswith(".png"):
    filename += ".png"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4
)

qr.add_data(data)
qr.make(fit=True)

image = qr.make_image(fill_color="black", back_color="white")

image.save(filename)

print("\n✅ QR Code Generated Successfully!")
print("Saved as:", filename)
