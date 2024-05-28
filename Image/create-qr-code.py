import qrcode
from PIL import Image
from urllib.parse import quote

qr_big = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
qr_big.add_data('https://flexitclothing.com')
qr_big.make()
img_qr_big = qr_big.make_image().convert('RGB')
img_qr_big.save(r'C:\Users\buy\flexitclothingQR.png')