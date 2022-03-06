from flask import Response, request
from database.models import Brevets
from flask_restful import Resource

class BrevetsAPI(Resource):
    def get(self):
        brevets = Brevets.objects().order_by('id').to_json()
        return Response(brevets,mimetype="application/json",status=200)
    def post(self):
        table = request.get_json()
        brevet = Brevets(**table).save()
        id = brevet.id
        return{'id':str(id)},200