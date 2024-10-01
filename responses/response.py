from .response_template.response_template import ResponseTemplate
from flask import jsonify


class Response:
    def __init__(self):
        self.data = {"version": "2.0", "template": None,
                     "context": None, "data": None}

    def set_template(self, template: ResponseTemplate):
        self.data['template'] = template()

    def jsonify(self):
        return jsonify(self.data)
