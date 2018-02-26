import qrcode
#import pillow
qr=qrcode.QRCode(version=3, box_size=5, border=0)
qr.add_data('wwer.sdfadsf')
img = qr.make_image()  
#img = img.convert('RGBA')
img.save('../A.PNG')