import base64
from app import lambda_handler

with open("test.jpg", "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read())
    event = {'body' : encoded_string}
    extracted_text = lambda_handler(event, None)

print(extracted_text)