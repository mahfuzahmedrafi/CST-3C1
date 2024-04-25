import barcode
from barcode.writer import ImageWriter

ean = barcode.get('ean13', '1502274722751921', writer=ImageWriter())
filename = ean.save('barcode')
print(f"Barcode saved as: {filename}")
