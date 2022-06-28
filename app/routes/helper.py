from flask import abort, make_response
from ..models.board import Board
from ..models.card import Card


def validate(id, type):
    try:
        id = int(id)
    except:
        return abort(make_response({"message": f"{type} {id} is invalid"}, 400))

    instance = type.query.get(id)

    if not instance:
        abort(make_response({"message": f"{type} {id} not found"}, 404))

    return instance
