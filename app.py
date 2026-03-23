import streamlit as st
from PIL import Image
import io

from utils.image_filters import apply_filter
from utils.ocr_utils import extract_text
from utils.format_convert import convert_image

# CONFIG
st.set_page_config(page_title="Image Processing & OCR App", layout="wide")
st.title("🖼️ Image Processing & OCR Web App")

uploaded_file = st.file_uploader("Upload an Image", type=["png", "jpg"])

if uploaded_file:
    image = Image.open(uploaded_file)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Original Image")
        st.image(image, use_container_width=True)

    with col2:
        option = st.selectbox(
            "Choose Operation",
            ["Format Conversion", "Image Filters", "OCR (Text Extraction)"]
        )

        # FORMAT CONVERSION
        if option == "Format Conversion":
            target_format = st.selectbox("Convert To", ["PNG", "JPEG"])

            if st.button("Convert"):
                try:
                    converted = convert_image(image, target_format)

                    st.image(Image.open(converted))

                except Exception as e:
                    st.error(f"Error: {e}")

        # FILTERS
        elif option == "Image Filters":
            filter_type = st.selectbox(
                "Select Filter",
                ["grayscale", "blur", "invert"]
            )

            if st.button("Apply Filter"):
                try:
                    result = apply_filter(image, filter_type)

                    st.image(result)

                    buf = io.BytesIO()
                    result.save(buf, format="PNG")

                    
                except Exception as e:
                    st.error(f"Error: {e}")

        # OCR
        elif option == "OCR (Text Extraction)":
            if st.button("Extract Text"):
                try:
                    text = extract_text(image)

                    st.text_area("Extracted Text", text, height=250)

                    st.download_button(
                        "Download Text",
                        data=text,
                        file_name="extracted.txt"
                    )

                except Exception as e:
                    st.error(f"OCR Error: {e}")
