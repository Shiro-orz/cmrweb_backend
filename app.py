from flask import Flask, request, jsonify 
from flask_cors import CORS
from funcs.rocmr import get_pr_data, create_data

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'hello world'

@app.route('/test', methods=['GET', 'POST'])
def test():
    #print(params)
    try:
        if request.method == 'POST':
            #print('try to get from post')
            val = request.json
            print(val)
        elif request.method == 'GET':
            #print('try to get from get')
            val = request.args
            print(val) 
    except Exception:
        print('no data from frontend')
    #print('begin to back')
    # data ={
    #     'src': 'flask',
    #     'tar': 'vue'
    # }
    data = get_pr_data(val['type'])
    return jsonify(data)

@app.route('/postfine', methods=['GET', 'POST'])
def fetch_data():
    try:
        if request.method == 'POST':
            val = request.json
            print(val)
        elif request.method == 'GET':
            val = request.args
            print(val) 
    except Exception:
        print('no data from frontend')
    data = create_data(val)
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')