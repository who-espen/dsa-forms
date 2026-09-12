import qrcode
from PIL import Image

def generate_qr_with_logo(url, logo_path, output_path="qr_dossier_day3.jpg"):
    """
    Generate a QR code with a centered logo (works with JPG files).

    Args:
        url (str): The URL to encode in the QR code
        logo_path (str): Path to the logo image file (JPG, PNG, etc.)
        output_path (str): Where to save the final QR code image
    """
    # Create QR code instance with high error correction
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction for logo
        box_size=10,
        border=5,
    )

    # Add data to QR code
    qr.add_data(url)
    qr.make(fit=True)

    # Create QR code image
    qr_img = qr.make_image(fill_color="black", back_color="white").convert('RGB')

    # Open logo (works with JPG, PNG, etc.)
    logo = Image.open(logo_path)

    # Calculate logo size (20% of QR code width)
    qr_width, qr_height = qr_img.size
    logo_size = int(qr_width * 0.2)
    logo = logo.resize((logo_size, logo_size), Image.LANCZOS)

    # Calculate position to center logo
    logo_pos = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)

    # Paste logo onto QR code
    qr_img.paste(logo, logo_pos)

    # Save the final image as JPG
    qr_img.save(output_path, quality=95)  # High quality for JPG output
    print(f"QR code with logo generated successfully as '{output_path}'")

# Example usage
if __name__ == "__main__":
    url = "https://dossier-workshop-day3.netlify.app/"
    logo_path = "logo-espen.jpg"  # Replace with your JPG logo file path

    generate_qr_with_logo(url, logo_path)
