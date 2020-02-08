import qrcode

qr = qrcode.QRCode (version = 1, box_size = 15, border=5)

data = "https://gfp-2a3tnpzj.stackpathdns.com/wp-content/uploads/2016/07/Shiba-Inu-1600x700.jpg"
qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill = "black", back_color  = "white")
img.save("Shiba_Inu.png")
