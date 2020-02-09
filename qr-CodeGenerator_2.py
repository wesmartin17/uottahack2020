import qrcode

qr = qrcode.QRCode (version = 1, box_size = 15, border=5)

data = "https://cdn-01.media-brady.com/store/stus/media/catalog/product/cache/4/image/85e4522595efc69f496374d01ef2bf13/1544626175/m/e/medical-alert-peanut-allergy-food-allergy-signs-l12150-lg.jpg"
qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill = "black", back_color  = "white")
img.save("Shiba_Inu.png")
