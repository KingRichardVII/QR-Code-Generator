# Richard Phan
# 10/8/25

#Import the qrcode package library
#builds the qr codes and renders them as images
import qrcode

# Prompt the user for input
link = input("Enter the link or text to encode: ")
box_size = int(input("Enter the box size (e.g., 10): "))
fill_color = input("Enter the fill color (e.g., red, blue, green): ")
back_color = input("Enter the background color (e.g., white, black): ")

# Create the QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=box_size, #grabs from user input
    border=2
)

qr.add_data(link) #stores text/URL in QR structure
qr.make(fit=True) #builds optimal matrix for content

# Generate, save, and print the image
img = qr.make_image(fill_color=fill_color, back_color=back_color)
img.save("coloredCode.png")
img.show()

print("QR code created and saved as 'coloredCode.png'.")
