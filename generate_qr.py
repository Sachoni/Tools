
# ==========================================================
# QR CODE GENERATOR
# ==========================================================

import qrcode
from pathlib import Path

website_url = "https://sachoni.github.io/LUDA-SERVICES/"

# ----------------------------------------------------------
# 2. OUTPUT FILE
# ----------------------------------------------------------

output_file = Path(__file__).parent / "luda_services_qr.png"

# ----------------------------------------------------------
# 3. GENERATE THE QR CODE
# ----------------------------------------------------------

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=12,
    border=4,
)

# Add the website URL to the QR code.
qr.add_data(website_url)
qr.make(fit=True)

# Create a professional black-and-white QR image.
qr_image = qr.make_image(
    fill_color="black",
    back_color="white"
)

# ----------------------------------------------------------
# 4. QR CODE
# ----------------------------------------------------------

qr_image.save(output_file)

print("======================================")
print("      LUDA SERVICES QR GENERATOR")
print("======================================")
print(f"Website: {website_url}")
print(f"QR code saved to: {output_file}")
print("======================================")
print("Scan the QR code with your phone camera.")
