from flask import abort, make_response
from .models.board import Board
import requests


def validate_board(id):
	try:
		id = int(id)
	except:
		return abort(make_response({"message": f"board {id} is invalid"}, 400))

	board = Board.query.get(id)

	if not board:
		abort(make_response({"message": f"board {id} not found"}, 404))

	return board