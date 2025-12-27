import fitz  # PyMuPDF
import os

pdf_path = "Engineering_Beyond_the_Vibe.pdf"
output_folder = "slides"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

doc = fitz.open(pdf_path)

for i in range(len(doc)):
    page = doc.load_page(i)
    pix = page.get_pixmap(matrix=fitz.Matrix(2, 2)) # 2x zoom for better quality
    output_file = f"{output_folder}/slide_{i+1}.png"
    pix.save(output_file)
    print(f"Saved {output_file}")

print("Done.")
