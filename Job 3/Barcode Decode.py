from pyzbar.pyzbar import decode
from PIL import Image

# Load the barcode image
barcode_image = Image.open('barcode.png')

# Decode the barcode
decoded_objects = decode(barcode_image)

# Print decoded barcode value
if decoded_objects:
    barcode_value = decoded_objects[0].data.decode('utf-8')
    print("Decoded barcode value:", barcode_value)
else:
    print("No barcode detected.")
