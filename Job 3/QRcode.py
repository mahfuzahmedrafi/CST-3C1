import qrcode

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data("Name: Mahfuz Ahmed Rafi\nRoll: 751921\nSemester: 3rd(Morning)\nDept: CST")
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("qrcode.png")

print(f"QRcode is saved")