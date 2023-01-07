from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route('/xyz', methods=['GET', 'POST'])
def test():
    if (request.method == 'POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a + b
        return jsonify(str(result))


@app.route('/abc', methods=['POST'])
def test2():
    if (request.method == 'POST'):
        a = request.json['num3']
        b = request.json['num4']
        result = a + b
        return jsonify(str(result))


@app.route('/mno', methods=['POST'])
def test3():
    if (request.method == 'POST'):
        a = request.json['num5']
        b = request.json['num6']
        result = a + b
        return jsonify(str(result))


@app.route('/pqr', methods=['POST'])
def test4():
    if (request.method == 'POST'):
        a = request.json['num7']
        b = request.json['num8']
        result = a + b
        return jsonify(str(result))


if __name__ == '__main__':
    app.run()