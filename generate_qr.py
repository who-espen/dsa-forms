import qrcode

# URL to encode
url = "https://ntd-data-workshop-day5.netlify.app/"

# Create QR code instance
qr = qrcode.QRCode(
    version=1,          # Controls the size of the QR Code (1-40)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
    box_size=10,        # Size of each box in pixels
    border=5,           # Border thickness in boxes
)

# Add data to the QR code
qr.add_data(url)
qr.make(fit=True)

# Create and save the QR code image
img = qr.make_image(fill_color="black", back_color="white")
img.save("ntd_workshop_qr_day5.png")

print("QR code generated successfully as 'ntd_workshop_qr.png'")
