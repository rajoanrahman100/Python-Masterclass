import qrcode

data=input("Enter the text or url: ").strip() # Get rid of any white spaces
fileName=input("Enter a file name: ").strip()

qr=qrcode.QRCode(box_size=1,border=5) # box_size is the size of each box in the QR code, border is the width of the border around the QR code
qr.add_data(data)
image=qr.make_image(fill_color="black",back_color="white")
image.save(fileName)
print(f"QR code saved as {fileName}.png")
