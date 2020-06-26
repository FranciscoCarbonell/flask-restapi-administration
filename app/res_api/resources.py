from app import api
from flask_restplus import Resource
from flask_jwt_extended import jwt_required
from app.models.player import Player, SerializerPLayer

@api.route('/players')
class PlayerResource(Resource):
    def get(self):
        splayer = SerializerPLayer(many=True)
        players = Player.query.all()
        return splayer.dump(players)
