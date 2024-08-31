import qrcode as qr
image = qr.make("https://www.instagram.com/")
image.save("Qr_code_instagram.png")