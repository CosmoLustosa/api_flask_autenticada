import json

from flask_restful import Resource
from utils import consulta_pessoas

lista_habilidades = ["Python", "Java", "C", "C++", "C#", "PHP"]


class Habilidades(Resource):
    def get(self):
        return lista_habilidades


class Pessoa(Resource):
    def get(self):
        dado = str(consulta_pessoas())
        return {'1': dado}
