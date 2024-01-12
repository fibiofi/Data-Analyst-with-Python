import PyPDF2
import os

os.chdir(r"C:\Users\asus\parse")

# Buka file PDF
pdfFile1 = open("laporan1.pdf", 'rb')
pdfFile2 = open("laporan2.pdf", 'rb')
pdfFile3 = open("laporan3.pdf", 'rb')

# Buat objek PdfReader
reader1 = PyPDF2.PdfReader(pdfFile1)
reader2 = PyPDF2.PdfReader(pdfFile2)
reader3 = PyPDF2.PdfReader(pdfFile3)

# Mendapatkan jumlah halaman
num_pages1 = len(reader1.pages)
num_pages2 = len(reader2.pages)
num_pages3 = len(reader3.pages)

# Looping melalui halaman-halaman dan melakukan ekstraksi teks
for page_num in range(num_pages1):
    page1 = reader1.pages[page_num]
    text1 = page1.extract_text()
    print(f"Laporan1 - Halaman {page_num + 1}:\n{text1}\n")

for page_num in range(num_pages2):
    page2 = reader2.pages[page_num]
    text2 = page2.extract_text()
    print(f"Laporan2 - Halaman {page_num + 1}:\n{text2}\n")

for page_num in range(num_pages3):
    page3 = reader3.pages[page_num]
    text3 = page3.extract_text()
    print(f"Laporan3 - Halaman {page_num + 1}:\n{text3}\n")

# Tutup file PDF
pdfFile1.close()
pdfFile2.close()
pdfFile3.close()
