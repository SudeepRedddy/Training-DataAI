import os
import shutil

path = r"C:\Users\sudee\Downloads\Capgemini\Python\DAY4\fileManager"

txt_dst  = r"C:\Users\sudee\Downloads\Capgemini\Python\DAY4\fileManager\txt"
pdf_dst  = r"C:\Users\sudee\Downloads\Capgemini\Python\DAY4\fileManager\pdf"
png_dst  = r"C:\Users\sudee\Downloads\Capgemini\Python\DAY4\fileManager\png"
docx_dst = r"C:\Users\sudee\Downloads\Capgemini\Python\DAY4\fileManager\docx"

os.makedirs(txt_dst, exist_ok=True)
os.makedirs(pdf_dst, exist_ok=True)
os.makedirs(png_dst, exist_ok=True)
os.makedirs(docx_dst, exist_ok=True)

for file in os.listdir(path):
    file_path = os.path.join(path, file)

    if os.path.isfile(file_path):
        if file.lower().endswith(".txt"):
            shutil.move(file_path, txt_dst)
            print(f"Moved TXT: {file}")

        elif file.lower().endswith(".pdf"):
            shutil.move(file_path, pdf_dst)
            print(f"Moved PDF: {file}")

        elif file.lower().endswith(".png"):
            shutil.move(file_path, png_dst)
            print(f"Moved PNG: {file}")

        elif file.lower().endswith(".docx"):
            shutil.move(file_path, docx_dst)
            print(f"Moved DOCX: {file}")

print("File organization completed")
