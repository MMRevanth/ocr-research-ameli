from PIL import Image
import pytesseract
print(pytesseract.image_to_string(Image.open('/home/revanth/Desktop/ocr-research-ameli/sample images/realme.png')))






