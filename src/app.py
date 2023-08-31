from PIL import Image
import pytesseract
import base64
from io import BytesIO

def lambda_handler(event, context):
    """
    Lambda function to perform OCR (Optical Character Recognition) on an image received as base64 encoded string.

    Args:
        event (dict): The event data containing the base64 encoded image in the 'body' field.
        context (object): Lambda function context.

    Returns:
        dict: A dictionary containing the extracted text from the image.
            {
                'text': 'Extracted text from the image'
            }
    """
    try:
        # Decode the base64 encoded image data
        img_b64dec = base64.b64decode(event['body'])
        # Create a BytesIO object from the decoded image data
        img_byteIO = BytesIO(img_b64dec)
        # Open the image using PIL
        image = Image.open(img_byteIO)

        # Perform OCR on the image using pytesseract
        extracted_text = pytesseract.image_to_string(image)

        # Return the extracted text as a response
        return {
            'text': extracted_text
        }
    except Exception as e:
        return {
            'error': str(e)
        }

# Sample usage
# event = {
#     'body': 'base64_encoded_image_string_here'
# }
# result = lambda_handler(event, None)
# print(result)
