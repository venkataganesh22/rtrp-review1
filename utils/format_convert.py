from PIL import Image
import io

def convert_image(pil_image, target_format):
    buf = io.BytesIO()

    # Save image in desired format
    pil_image.save(buf, format=target_format)

    buf.seek(0)  # move pointer to beginning

    return buf
