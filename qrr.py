import qrcode as qr
img = qr.make("https://www.amazon.in/")
img.save("QRCode.png")
