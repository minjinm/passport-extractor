from PIL import Image
import pytesseract
import re

def extract_passport_data(image_path):
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img)

    passport_data = {
        "Name": re.search(r'P<\w+<([\w<]+)', text).group(1).replace("<", " ") if re.search(r'P<\w+<([\w<]+)', text) else "Unknown",
        "Passport_Number": re.search(r'\b[A-Z0-9]{8,9}\b', text).group() if re.search(r'\b[A-Z0-9]{8,9}\b', text) else "Unknown"
    }

    return passport_data, text
