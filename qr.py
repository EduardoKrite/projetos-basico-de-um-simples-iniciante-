#precisa instalar pip install qrcode cara criar um qrcode
# e o pip install Pillowp precisa para gera a foto 
import qrcode 
#digita para criar um qrcode
data = input("Digita o codigo para gera um qrcode: ")
# o tamanho do qrcode
qr = qrcode.QRCode(version=1,border=5,box_size=10)
#Criar o qrcode
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image()
img.save("qrcode.png")
