import qrcode

qr = qrcode.QRCode(version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_H,
                    box_size=10, #adjust size of qr code
                    border=2)

qr.add_data("https://www.youtube.com/watch?v=IX0RvTEVtDw") #insert whatever link you want
qr.make(fit=True)

img = qr.make_image(fill_color ="red", back_color ="black") #swap colors with the ones you want
img.save("coloredCode.png")
img.show()

#Next steps:
#Ask user for input of variables, including box size, fill color, and background color, as well as link.

