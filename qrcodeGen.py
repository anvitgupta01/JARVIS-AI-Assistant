import pyqrcode
s = input("Enter the data or text to be encoded in QR code...")
f = input("Input the name of the file in which QR Code have to be saved along with extension...")

url = pyqrcode.create(s) 
if (f.endswith("svg")) :
    url.svg(f, scale = 8) 
else :
    url.png(f, scale = 8) 