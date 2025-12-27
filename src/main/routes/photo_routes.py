from flask import Blueprint, jsonify, request
from src.views.http_types.http_request import HttpRequest

from src.main.composer.photo_creator_composer import photo_creator_composer
from src.main.composer.photo_finder_composer import photo_finder_composer
from src.main.composer.photo_lister_composer import photo_lister_composer
from src.main.composer.photo_deleter_composer import photo_deleter_composer

from src.errors.error_handler import handle_errors

photo_route_bp = Blueprint("photos_routes", __name__)

@photo_route_bp.route("/photos", methods=["POST"])
def create_photo():
    try:
        http_request = HttpRequest(body=request.json)
        view = photo_creator_composer()

        http_response = view.handle(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code
    

@photo_route_bp.route("/photos/<photo_id>", methods=["GET"])
def find_photo_by_id(photo_id):
    try:
        http_request = HttpRequest(param={ "photo_id": photo_id })
        view = photo_finder_composer()

        http_response = view.handle(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code


@photo_route_bp.route("/photos", methods=["GET"])
def list_photos():
    try:
        http_request = HttpRequest()
        view = photo_lister_composer()

        http_response = view.handle(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code


# @photo_route_bp.route("/albums/<album_id>", methods=["DELETE"])
# def delete_album(album_id):
#     try:
#         http_request = HttpRequest(param={ "album_id": album_id })
#         view = album_deleter_composer()

#         http_response = view.handle(http_request)
#         return jsonify(http_response.body), http_response.status_code
#     except Exception as exception:
#         http_response = handle_errors(exception)
#         return jsonify(http_response.body), http_response.status_code
