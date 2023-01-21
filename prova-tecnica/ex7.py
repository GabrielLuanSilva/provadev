import http
import json

from flask import Flask, request, Response

app = Flask(__name__)


@app.route('/soma', methods=['POST'])
def soma() -> Response:
    response = request.json
    return Response(
        response=json.dumps({'resultado': response['y'] + response['x']}),
        status=http.HTTPStatus.OK,
        mimetype='application/json'
    )


if __name__ == '__main__':
    app.run(debug=True)
