from http import HTTPStatus

from flask import Blueprint, jsonify, request

from template.lib import example

hello_api = Blueprint("hello_api", __name__)


@hello_api.route("")
def hello():
    example.test()

    ret = {
        "status": HTTPStatus.OK,
        "msg": "hello",
    }
    return jsonify(ret), ret["status"]
