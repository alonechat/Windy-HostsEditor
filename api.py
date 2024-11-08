from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def api():
    data = request.get_json()
    try:
        if requests['names'] is not None:
        
            pass
    except IndexError:
        pass
    return jsonify(response)

if __name__ == '__main__':
    app.run(port=5000)
