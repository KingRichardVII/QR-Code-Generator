#Richard Phan
#9/23/25

#import qrcode library (ensure pip install qrcode installed in virtual environment first)
import qrcode

#Create QR code that points to YouTube vid
img = qrcode.make("https://www.youtube.com/watch?v=X7RotIysnpo")
img.save("mycode.png")
img.show() #opens in default image viewer

