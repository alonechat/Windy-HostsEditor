from flask import Flask, request, jsonify
import main

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def api():
    data = request.get_json()
    try:
        if requests['names'] is not None:
            ips = requests['names']['pairs']:
            
            for keys in list(ips.keys()):
                
                main.update_hosts_file(
                    str(list(keys)), 
                    str(ips[keys])
                )
    except IndexError:
        pass
    return jsonify(response)

if __name__ == '__main__':
    app.run(port=5000)
