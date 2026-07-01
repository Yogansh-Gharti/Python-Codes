import os
from PyPDF2 import PdfMerger

print("===== PDF MERGER TOOL =====")

pdf_files = []

while True:
    pdf = input("Enter PDF file path (or type 'done'): ")

    if pdf.lower() == "done":
        break

    if os.path.exists(pdf) and pdf.lower().endswith(".pdf"):
        pdf_files.append(pdf)
    else:
        print("❌ Invalid PDF file!")

if len(pdf_files) < 2:
    print("Please provide at least 2 PDF files.")
    exit()

output_name = input("Enter Output PDF Name: ")

if not output_name.endswith(".pdf"):
    output_name += ".pdf"

merger = PdfMerger()

try:
    for pdf in pdf_files:
        merger.append(pdf)

    merger.write(output_name)
    merger.close()

    print(f"\n✅ PDFs merged successfully!")
    print(f"Saved as: {output_name}")

except Exception as e:
    print("Error:", e)
