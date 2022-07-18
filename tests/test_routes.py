from app.models.board import Board
import pytest


def test_get_boards(client, all_boards):
    # Act
    response = client.get("/boards")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == [
        {'board_id': 1, 'owner': 'Jande', 'title': 'New board 1'},
        {'board_id': 2, 'owner': 'Emily', 'title': 'New board 2'},
        {'board_id': 3, 'owner': 'Ivana', 'title': 'New board 3'}]


def test_get_one_board(client, one_board):
    response = client.get("/boards/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert "board" in response_body
    assert response_body == {
        "board": {
            "board_id": 1,
            "title": "Create new board",
            "owner": "Emily",
        }
    }


def test_get_board_not_found(client):
    # Act
    response = client.get("/boards/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert response_body == {
        "message": "<class 'app.models.board.Board'> 1 not found"}


def test_create_board(client):
    # Act
    response = client.post("/boards", json={
        "title": "Created a New Board",
        "owner": "Emily",
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert "board" in response_body
    assert response_body == {
        "board": {
            "board_id": 1,
            "title": "Created a New Board",
            "owner": "Emily",
        }
    }


def test_create_board_missing_title(client):
    # Act
    response = client.post("/boards", json={})
    response_body = response.get_json()

    # Assert
    assert response.status_code == 400
    assert response_body == {
        "details": "Invalid data"
    }


def test_update_board(client, one_board):
    # Act
    response = client.put("/boards/1", json={
        "title": "Updated Board Title",
        "owner": "Jande"
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert "board" in response_body
    assert response_body == {
        "board": {
            "board_id": 1,
            "title": "Updated Board Title",
            "owner": "Jande"
        }
    }
    board = Board.query.get(1)
    assert board.title == "Updated Board Title"


def test_update_board_not_found(client):
    # Act
    response = client.put("/boards/1", json={
        "title": "Updated Board Title"
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert response_body == {
        "message": "<class 'app.models.board.Board'> 1 not found"}


def test_delete_board(client, one_board):
    # Act
    response = client.delete("/boards/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert "details" in response_body
    assert response_body == {
        "details": 'Board 1 "Create new board" successfully deleted'
    }


def test_delete_board_not_found(client):
    # Act
    response = client.delete("/boards/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert response_body == {
        "message": "<class 'app.models.board.Board'> 1 not found"}
    assert Board.query.all() == []
