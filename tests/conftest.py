import pytest
from app import create_app
from app import db
from app.models.board import Board


@pytest.fixture
def app():
    # create the app with a test config dictionary
    app = create_app({"TESTING": True})

    with app.app_context():
        db.create_all()
        yield app

    # close and remove the temporary database
    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def one_board(app):
    new_board = Board(
        title="Create new board", owner="Emily")
    db.session.add(new_board)
    db.session.commit()


@pytest.fixture
def all_boards(app):
    board1 = Board(
        title="New board 1", owner="Jande")
    board2 = Board(
        title="New board 2", owner="Emily")
    board3 = Board(
        title="New board 3", owner="Ivana")
    db.session.add_all([board1, board2, board3])
    db.session.commit()
