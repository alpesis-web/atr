from flask import Blueprint, jsonify, request

from utils.sqlalchemy import db

from models.dream import Dream


blueprint = Blueprint('dreams', __name__, url_prefix='/api/v0/dreams')

@blueprint.route('', methods=['POST'])
def post():

    dream = Dream()
    dream.from_json(request.get_json())
    db.session.add(dream)
    db.session.commit()
    return _api_response(dream) 

@blueprint.route('/<int:id>', methods=['GET'])
def get(id):
    dream = Dream.query.get_or_404(id)
    return _api_response(dream)

@blueprint.route('/<int:id>', methods=['PUT', 'PATCH'])
def update(id):
    dream = Dream.query.get_or_404(id)
    dream.from_json(request.get_json())
    db.session.commit()
    return _api_response(dream)

@blueprint.route('/<int:id>', methods=['DELETE'])
def delete(id):
    Dream.query.filter_by(id=id).delete()
    db.session.commit()
    return jsonify() 

def _api_response(dream):
    return jsonify(**dream.to_json())
