from flask import Response, request
from database import Brevets
from flask_restful import Resource

class BrevetsAPI(Resource):
    def get(self):
        brevets = Brevet.objects().order_by('id').to_json()
        return Response(brevets,mimetype="application/json",status=200)
    def post(self):
        table = request.get_json()
        brevet = Brevet(**table).save()
        id = brevet.id
        return{'id':str(id),'status':created},200