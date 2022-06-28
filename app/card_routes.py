from flask import Blueprint, request, jsonify, make_response
from app import db
from app.helper import validate_card
from app.models.card import Card
from app.models.board import Board
from app.helper import validate_card

# Blueprint: 
card_bp = Blueprint('card_bp', __name__, url_prefix="/cards")


# CREATE new card:
@card_bp.route("", methods = ["POST"])
def create_card():
    request_body = request.get_json()
    
    new_card = Card.create(request_body)

    db.session.add(new_card)
    db.session.commit()

    return make_response({"card": new_card.to_json()}, 201)

# GET ALL cards:
@card_bp.route("", methods = ["GET"])
def get_all_cards():
    cards = Card.query.all()
    cards_response = [cards.to_json() for card in cards]

    return jsonify(cards_response), 200

# GET ONE card:
@card_bp.route("/<id>", methods = ["GET"])
def get_one_card(id): 
    card = validate_card(id)

    return jsonify({"card": card.to_json()}), 200

# UPDATE one card:
@card_bp.route("/<id>", methods = ["PUT"])
def update_card(id):
    card = validate_card(id)
    request_body = request.get_json()
    card.update(request_body)

    db.session.commit()

    return jsonify({"card": card.to_json()}), 200

# DELETE card:
@card_bp.route("/<id>", methods = ["DELETE"])
def delete_card(id): 
    card = validate_card(id)

    db.session.delete(card)
    db.session.commit()

    return jsonify({"details": f"Card {id} successfully deleted"}), 200
