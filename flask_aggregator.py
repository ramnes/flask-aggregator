import json

from flask import request, Response
from werkzeug.exceptions import BadRequest
from werkzeug.test import EnvironBuilder


class Aggregator(object):

    def __init__(self, app=None, endpoint=None):
        self.url_map = {}
        self.endpoint = endpoint or "/aggregate"
        if app:
            self.init_app(app)

    def init_app(self, app):
        app.add_url_rule(self.endpoint, view_func=self.post, methods=["POST"],
                         defaults={"app": app})

    def get_response(self, app, route):
        query_string = ""
        if '?' in route:
            route, query_string = route.split('?', 1)

        builder = EnvironBuilder(path=route, query_string=query_string)
        app.request_context(builder.get_environ()).push()
        return app.dispatch_request()

    def post(self, app):
        try:
            data = request.data.decode('utf-8')
            routes = json.loads(data)
            if not isinstance(routes, list):
                raise TypeError
        except (ValueError, TypeError) as e:
            raise BadRequest("Can't get requests list.")

        def __generate():
            data = None
            for route in routes:
                yield data + ', ' if data else '{'
                response = self.get_response(app, route)
                json_response = json.dumps(response)
                data = '"{}": {}'.format(route, json_response)
            yield data + '}'

        return Response(__generate(), mimetype='application/json')
