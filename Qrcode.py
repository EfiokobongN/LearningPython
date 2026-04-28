import pyqrcode

url = input('enter your website link to generate qrcode : \n')
QR = pyqrcode.create(url)
QR.png("qrcode.png", scale=9)