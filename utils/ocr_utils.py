import easyocr
import numpy as np

# Load once (important for performance)
_reader = None

def get_reader():
    global _reader
    if _reader is None:
        _reader = easyocr.Reader(['en'], gpu=False)
    return _reader

def extract_text(pil_image):
    # Convert PIL → NumPy
    image = np.array(pil_image)

    reader = get_reader()
    results = reader.readtext(image)

    # Extract only text
    text = " ".join([res[1] for res in results])

    return text
  
