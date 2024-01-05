import qrcode
data = input("Enter data or site to encode in the QR ...")
image = input("Input the file name along with extension for QR to be saved into ")
qr = qrcode.QRCode(version = 1,
                error_correction = qrcode.constants.ERROR_CORRECT_H,   
				box_size = 10,
				border = 5)
qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill_color = 'black',
					back_color = 'white')
img.save(f'{image}')