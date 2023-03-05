from flask import Flask, jsonify, request
import os
import json
#from pi import Pi

app = Flask(__name__)

pis = {}

class Pi:
    def __init__(self, name, ip, network, tag, timestamp, status= 'GREEN'):
        self.name = name
        self.ip = ip
        self.network = network
        self.tag = tag
        self.timestamp = timestamp
        self.status = status


@app.route('/')
def index():
    return jsonify({"HelloWorld": "Welcome to Pi-Dir"})

@app.route('/pis', methods=['GET'])
def getPis():
    #TODO: return the pis dict instead of this fake object
    pi = Pi("name","192.168.1.99","network","tag","timestamp")
    return json.dumps(pi.__dict__)

@app.route('/pis', methods=['POST'])
def postPi():
    data = request.get_json()
    if data is None:
        return jsonify({ 'error': 'Missing input' }), 400
    
    # Get the data from the posting
    name = data.get('name', None)
    ip = data.get('ip', None)
    network = data.get('network')
    tag =data.get('tag')

    #Validate that name and pi are set
    if name is None:
        return jsonify({ 'error': 'Missing input' }), 400
    
    if ip is None:
        return jsonify({ 'error': 'Missing input' }), 400
    

    #create a new object. 
    newPi = Pi(name, ip , network, tag, "")
    # TODO: Add it to the Dict called pis
    global pis
    return json.dumps(newPi.__dict__)

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
