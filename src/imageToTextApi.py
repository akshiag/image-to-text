from flask import Flask, request, jsonify
from app import lambda_handler

app = Flask(__name__)

@app.route('/', methods=['POST'])
def extract_text():
    try:
        # Get base64 encoded image from the request
        image_data = request.get_data()
        event = {'body' : image_data}
        extracted_text = lambda_handler(event, None)

        return jsonify({'text': extracted_text})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)



