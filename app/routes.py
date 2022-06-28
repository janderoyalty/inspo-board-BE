from crypt import methods
from flask import Blueprint, request, jsonify, make_response
from app import db
from app.models.board import Board
from app.helper import validate_board

# example_bp = Blueprint('example_bp', __name__)
board_bp = Blueprint('board_bp', __name__, url_prefix="/boards")
card_bp = Blueprint('card_bp', __name__, url_prefix="/cards")

# ********* BOARD *********
# CREATE new board
# CREATE BOARD - "/boards" - POST
@board_bp.route("", methods = ["POST"])
def create_board():
    pass

# READ all boards
# GET ALL BOARDS - "/boards" - GET
@board_bp.route("", methods = ["GET"])
def get_all_boards():
    pass

# READ one board
# GET ONE BOARDs - "/boards/1" - GET
@board_bp.route("/<id>", methods = ["GET"])
def get_one_board():
    pass

# UPDATE cards
# UPDATE BAORD - "/boards/cards/1" - PUT
@board_bp.route("/cards/<id>", methods = ["PUT"])
def update_board():
    pass

# DELETE board
# UPDATE BAORD - "/boards/1" - DELETE
@board_bp.route("/<id>", methods = ["DELETE"])
def delete_board():
    pass

