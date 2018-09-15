import io
import os

# Google Cloud APIs
from google.cloud import vision

def image_ocr(file_path):
    # Get client
    client = vision.ImageAnnotatorClient()

    # Image raw bytes
    with io.open(file_path, 'rb') as file:
        content = file.read()

    image = vision.types.Image(content=content)
    # Perform OCR through cloud
    response = client.text_detection(image=image)
    # Hard code field values
    text = response.text_annotations[0].description

    return text


def split_str_and_get_quoted(text):
    strs = text.split('\"')
    quoted_indices = list(range(1, len(strs), 2))
    return strs, quoted_indices


if __name__ == '__main__':
    text = image_ocr('test-txt.jpeg')
    strs, quoted_indices = split_str_and_get_quoted(text)





