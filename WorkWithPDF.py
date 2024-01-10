from PyPDF2 import PdfWriter, PdfReader, PdfMerger

def encrypt():
    FILE = input("Enter the full path of file to encrypt ")
    out = PdfWriter()
    file = PdfReader(FILE)
    num = len(file.pages)
    for idx in range(num):
        page  = file.pages[idx]
        out.add_page(page)
    password = input("Enter the password for encryption ")
    out.encrypt(password)
    with open("Resume_encrypted.pdf","wb") as w:
        out.write(w)
    return

def decrypt():
    FILE = input("Enter the full path of file to decrypt ")
    password = input("Enter the password for decryption ")
    out = PdfWriter()
    file = PdfReader(FILE)
    if file.is_encrypted:
        file.decrypt(password)
        num = len(file.pages)
        for idx in range(num):
            page  = file.pages[idx]
            out.add_page(page)
        with open("Resume_decrypted.pdf","wb") as w:
            out.write(w)
    else:
        print("File already decrypted ")
    return

# Assumption that all files are already decrypted :
def merge():
    numFiles = input("Number of files to merge")
    numFiles = int(numFiles)
    merger = PdfMerger()
    for x in range(numFiles):
        FILE = input("Enter the file full path to merge ")
        merger.append(FILE)
    with open("FILES_Merged.pdf","wb") as f:
        merger.write(f)
    return