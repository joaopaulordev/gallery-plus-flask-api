from flask import Blueprint, jsonify, request
from src.views.http_types.http_request import HttpRequest

from src.main.composer.album_creator_composer import album_creator_composer
from src.main.composer.album_finder_composer import album_finder_composer
from src.main.composer.album_lister_composer import album_lister_composer
from src.main.composer.album_deleter_composer import album_deleter_composer

from src.errors.error_handler import handle_errors

album_route_bp = Blueprint("albums_routes", __name__)


@album_route_bp.route("/albums", methods=["POST"])
def create_album():
    try:
        http_request = HttpRequest(body=request.json)
        view = album_creator_composer()

        http_response = view.handle(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code
    

@album_route_bp.route("/albums/<album_id>", methods=["GET"])
def find_album_by_id(album_id):
    try:
        http_request = HttpRequest(param={ "album_id": album_id })
        view = album_finder_composer()

        http_response = view.handle(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code


@album_route_bp.route("/albums", methods=["GET"])
def list_albums():
    try:
        http_request = HttpRequest()
        view = album_lister_composer()

        http_response = view.handle(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code


@album_route_bp.route("/albums/<album_id>", methods=["DELETE"])
def delete_album(album_id):
    try:
        http_request = HttpRequest(param={ "album_id": album_id })
        view = album_deleter_composer()

        http_response = view.handle(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code
