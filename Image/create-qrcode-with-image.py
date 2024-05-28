import qrcode
from PIL import Image
from urllib.parse import quote

face = Image.open(r'C:\Users\buy\OneDrive\Dokumente\Visuals\Presskits\Bitcoin\bitcoin-btc-logo.png')\
	.resize((282, 282))
print(face.size)
qr_big = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
body = quote('Sehr geehrter Herr Laubenheimer, \n\n Ich möchte an dem Workshop,\
	\"Einführung in die Welt der Blockchains\", teilnehmen.\
	\n\n Meine Zeitpräferenzen sind: <Hier_Ihre_zeitlichen_Präferenzen_einfügen>\
	\n\n Mit freundlichen Grüßen,\n\n <Hier_Ihren_Namen_Einfügen>')
qr_big.add_data(
	'mailto:workshop@laubenheimer.eu?subject=Workshop im Gemeindehaus Berkersheim, Mai&body=' + body)
qr_big.make()
img_qr_big = qr_big.make_image().convert('RGB')
pos = ((img_qr_big.size[0] - face.size[0]) // 2, (img_qr_big.size[1] - face.size[1]) // 2)
img_qr_big.paste(face, pos)
img_qr_big.save(r'C:\Users\buy\mailtoworkshopwithbitcoin.png')