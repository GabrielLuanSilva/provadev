import http

from flask import Flask, request, Response, json

app = Flask(__name__)

count: int = 0


@app.route('/contador', methods=['POST', 'GET', 'DELETE'])
def contador() -> Response:
    global count
    if request.method == 'POST':
        count = request.json['numero']
        return Response(
            status=http.HTTPStatus.CREATED
        )
    elif request.method == 'GET':
        return Response(
            response=json.dumps({'numero': count}),
            status=http.HTTPStatus.OK,
            mimetype='application/json'
        )
    else:
        count = 0
        return Response(
            status=http.HTTPStatus.ACCEPTED)


@app.route('/contador/incrementa', methods=['PUT'])
def incrementa() -> Response:
    global count
    if count == 0:
        return Response(
            response=json.dumps({'erro': 'contador não iniciado'}),
            status=http.HTTPStatus.BAD_REQUEST,
            mimetype='application/json')
    else:
        count += 1
        return Response(
            status=http.HTTPStatus.ACCEPTED
        )


if __name__ == '__main__':
    app.run(debug=True)
