import json

from flask import request as current_request, Response
from werkzeug.exceptions import BadRequest


class Aggregator(object):

    def __init__(self, app=None, endpoint=None):
        self.url_map = {}
        self.endpoint = endpoint or "/aggregator"
        if app:
            self.init_app(app)

    def init_app(self, app):
        self.client = app.test_client()
        app.add_url_rule(self.endpoint, view_func=self.post, methods=["POST"])

    def post(self):
        try:
            requests = json.loads(current_request.data)
            if not isinstance(requests, list):
                raise TypeError
        except (ValueError, TypeError):
            raise BadRequest("Can't get requests list.")

        def __generate():
            data = None
            for request in requests:
                yield data + ',' if data else '{'
                data = '"{}": {}'.format(request, self.client.get(request).data)
            yield data + '}'

        return Response(__generate(), mimetype='application/json')
