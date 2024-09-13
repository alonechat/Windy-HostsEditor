from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def api():
    data = request.get_json()
    # DB ops is hidden...
    response = {
        'message': 'Hello, this is a simple Python API server!',
        'received_data': data
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(port=5000)
