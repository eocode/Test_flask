from flask import Blueprint
from app.utilities.responses import response, not_found
from models.msg import Msg

api_v1 = Blueprint('api_v1', __name__, url_prefix='/api/v1')


@api_v1.route('/msgs', methods=['GET'])
def get_msgs():
    msgs = Msg.query.all()
    return response([msg.serialize() for msg in msgs])


@api_v1.route('/msgs/<id>', methods=['GET'])
def get_msg(id):
    msg = Msg.query.filter_by(id=id).first()
    if msg is None:
        return not_found()
    return response(msg.serialize())


@api_v1.route('/msgs/<id>', methods=['POST'])
def create_msg():
    pass


@api_v1.route('/msgs/<id>', methods=['PUT'])
def update_msg():
    pass


@api_v1.route('/msgs/<id>', methods=['DELETE'])
def delete_msg():
    pass
