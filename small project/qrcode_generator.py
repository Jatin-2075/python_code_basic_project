import qrcode

a = input("enter the text you want in qr \n")
b = input("enter the file name along with file type 'png','jpeg' \n")

qr = qrcode.QRCode(version = 1,
                   error_correction=qrcode.constants.ERROR_CORRECT_H,
                   box_size=9,border=3
                   )

qr.add_data(a)
qr.make(fit=True)
img=qr.make_image(fill_color="red",back_color="white")
img.save(b)