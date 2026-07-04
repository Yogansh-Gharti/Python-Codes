import os
from PIL import Image

SUPPORTED_FORMATS = (".jpg", ".jpeg", ".png", ".webp")


def resize_and_compress(input_folder, output_folder, width, height, quality):
    if not os.path.exists(input_folder):
        print("❌ Input folder not found!")
        return

    os.makedirs(output_folder, exist_ok=True)

    processed = 0

    for file in os.listdir(input_folder):

        if file.lower().endswith(SUPPORTED_FORMATS):

            input_path = os.path.join(input_folder, file)
            output_path = os.path.join(output_folder, file)

            try:
                image = Image.open(input_path)

                image = image.resize((width, height))

                image.save(
                    output_path,
                    optimize=True,
                    quality=quality
                )

                print(f"✅ Processed: {file}")
                processed += 1

            except Exception as e:
                print(f"❌ Error processing {file}")
                print(e)

    print("\n===== SUMMARY =====")
    print(f"Images Processed: {processed}")
    print(f"Saved To: {output_folder}")


print("===== IMAGE RESIZER & COMPRESSOR =====")

input_folder = input("Enter Input Folder: ")
output_folder = input("Enter Output Folder: ")

width = int(input("New Width: "))
height = int(input("New Height: "))

quality = int(input("Compression Quality (1-100): "))

resize_and_compress(
    input_folder,
    output_folder,
    width,
    height,
    quality
)
