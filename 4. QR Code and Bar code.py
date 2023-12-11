import qrcode 

qr = qrcode.QRCode(
    version = 1,
    box_size = 10,
    border = 7
)
data = "https://www.facebook.com/NativeBuilder"
qr.add_data(data)
qr.make(fit=True)
image = qr.make_image(fill = "black", back_color="white")
image.save('Native Builders Fb QR.png')


