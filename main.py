from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

def is_trusted_url(url):
    # Your URL trust verification logic here
    return url.startswith("https://")

@app.route('/check_url', methods=['POST'])
def check_url():
    data = request.get_json()

    if 'url' not in data:
        return jsonify({'error': 'URL not provided'}), 400

    url = data['url']
    is_trusted = is_trusted_url(url)

    return jsonify({'url': url, 'is_trusted': is_trusted})

@app.route('/current_time', methods=['GET'])
def current_time():
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return jsonify({'current_time': current_time})

if __name__ == '__main__':
    app.run(debug=True)
