# Generate QR codes and save them into database of M2
import qrcode

#Link for website - this is just dummy data for us as QR codes will be assigned to each individual by internal system
input_data = "https://www.imdb.com/name/nm0000288/"

#create QR Code
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5
)

qr.add_data(input_data)
qr.make(fit=True)

img = qr.make_image(fill='black', back_color='white')
img.save('qrcode002.png')


