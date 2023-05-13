from flask import Flask, request, json, jsonify

app = Flask(__name__)


@app.route('/', methods=['POST'])
def webhook():
    if request.headers['Content-Type'] == 'application/json':
        result = json.dumps(request.json)
        print(result)
    
    return jsonify({'message': 'Received event'})

if __name__ == '__main__':
    app.run(debug=True)
