import cv2
import numpy as np
from PIL import Image

def apply_filter(pil_image, filter_type):
    # Convert PIL → NumPy (OpenCV uses BGR)
    image = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)

    if filter_type == "grayscale":
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    elif filter_type == "blur":
        image = cv2.GaussianBlur(image, (7, 7), 0)

    elif filter_type == "invert":
        image = cv2.bitwise_not(image)

    # Convert back to PIL
    if len(image.shape) == 2:  # grayscale
        return Image.fromarray(image)
    else:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        return Image.fromarray(image)
