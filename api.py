from flask import Flask, request, jsonify
import main

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def api():
    data = request.get_json()
    try:
        if requests['names'] is not None:
        
            main.
    except IndexError:
        pass
    return jsonify(response)

if __name__ == '__main__':
    app.run(port=5000)
