from flask import Flask, request

app = Flask(__name__)

@app.route('/json-example', methods=['POST'])
def json():
    data = request.get_json()
    ssid = data['ssid']
    passwd = data['password']

    path = '/home/conan94/flask/tmp.txt/'
    with open(path, "w") as f:
        f.write('hello world')

    return '''
        ssid : {}
        password : {}
        '''.format(ssid, passwd)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
