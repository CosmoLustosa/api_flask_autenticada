from flask import Flask, request
from flask_restful import Resource, Api
from habilidades import Habilidades, Pessoa
import json

app = Flask(__name__)
api = Api(app)

desenvolvedores = [
    {
        "id": 1,
        "nome": "Cosmo Lusotsa",
        "habilidades": ["Java", "C", "Pytohn"]
    },
    {
        "id": 2,
        "nome": "Ana Rell",
        "habilidades": ["C", "Pytohn"]
    },
    {
        "id": 3,
        "nome": "Marco Rocha",
        "habilidades": ["Fortran", "Pytohn", "Julia"]
    },
    {
        "id": 4,
        "nome": "Anonymous",
        "habilidades": ["C", "Assembly", "C#"]
    }
]


class Desenvolvedor(Resource):
    def get(self, id: int):
        try:
            response = desenvolvedores[id - 1]

        except IndexError:
            mensagem = f"Desenvolvedor de ID {id} não existe!"
            response = {'status': 'error', 'message': mensagem}
        except Exception:
            mensagem = "Erro desconhecido, procure o admin da API!"
            response = {'status': 'error', 'message': mensagem}

        return response

    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id - 1] = dados
        print(dados)
        return dados

    def delete(self, id):
        desenvolvedores.pop(id - 1)
        mensagem = "Sucesso, dev excluido..."
        return {'status': 'OK', 'message': mensagem}


class ListaDevs(Resource):
    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        mensagem = "Sucesso, dev adicionado..."
        return {'status': 'OK', 'message': mensagem}

    def get(self):
        return desenvolvedores


# adiciona as rotas na api
api.add_resource(Desenvolvedor, '/dev/<int:id>/')
api.add_resource(ListaDevs, '/dev/')
api.add_resource(Habilidades, '/habilidades/')
api.add_resource(Pessoa, '/')

if __name__ == '__main__':
    app.run(debug=True)
