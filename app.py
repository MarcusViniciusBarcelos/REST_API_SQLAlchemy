from flask import (Flask,
                   request)
from flask_restful import (Resource,
                           Api)
from models import (Pessoas,
                    Atividades)

app = Flask(__name__)
api = Api(app)


class Pessoa(Resource):
    def get(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        try:
            response = {
                'nome': pessoa.nome,
                'idade': pessoa.idade,
                'id': pessoa.id
            }
        except AttributeError:
            response = {
                'status': 'error',
                'mensagem': 'Pessoa não encontrada'
            }
        return response

    def put(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        try:
            dados = request.json
            if 'nome' in dados:
                pessoa.nome = dados['nome']
            if 'idade' in dados:
                pessoa.idade = dados['idade']
            pessoa.save()
            response = {
                'id': pessoa.id,
                'nome': pessoa.nome,
                'idade': pessoa.idade
            }
        except AttributeError:
            response = {
                'status': 'error',
                'mensagem': 'Pessoa não encontrada'
            }
        return response

    def delete(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        try:
            pessoa.delete()
            response = {
                'status': 'sucesso', 'mensagem': f'Pessoa {pessoa.nome} Excluída com sucesso'
            }
        except AttributeError:
            response = {
                'status': 'error',
                'mensagem': 'Pessoa não encontrada'
            }
        return response


class ListaPessoas(Resource):
    def get(self):
        pessoas = Pessoas.query.all()
        try:
            response = [{'id': i.id, 'nome': i.nome, 'idade': i.idade} for i in pessoas]
        except AttributeError:
            response = {
                'status': 'error',
                'mensagem': 'Nenhuma Pessoa cadastrada'
            }
        return response

    def post(self):
        dados = request.json
        try:
            pessoa = Pessoas(nome=dados['nome'], idade=dados['idade'])
            pessoa.save()
            response = {
                'id': pessoa.id,
                'nome': pessoa.nome,
                'idade': pessoa.idade
            }
        except AttributeError:
            response = {
                'status': 'error',
                'mensagem': 'Entrar em contato com o adm'
            }
        return response


class Atividade(Resource):
    def get(self, id):
        atividades = Atividades.query.get(id)
        try:
            response = {'id': atividades.id,
                        'nome': atividades.nome,
                        'pessoa': atividades.pessoa.nome}
        except AttributeError:
            response = {
                'status': 'error',
                'mensagem': 'Nenhuma tarefa encontrada'
            }
        return response

    def put(self, id):
        atividade = Atividades.query.get(id)
        try:
            data = request.get_json()
            if 'status' in data:
                atividade._status = data['status']
                atividade.save()
            response = {
                'status': 'sucesso',
                'mensagem': 'Atividade atualizada'
            }
        except AttributeError:
            response = {
                'status': 'error',
                'mensagem': 'Nenhuma tarefa encontrada'
            }
        return response

    def delete(self,id):
        atividade = Atividades.query.get(id)
        try:
            atividade.delete()
            response = {
                'status': 'sucesso', 'mensagem': f'atividade do dev {atividade.pessoa} Excluída com sucesso'
            }
        except AttributeError:
            response = {
                'status': 'error',
                'mensagem': 'atividade não encontrada'
            }
        return response


class ListaAtividades(Resource):
    def get(self):
        atividades = Atividades.query.all()
        response = [{'id': i.id, 'nome': i.nome, 'pessoa': i.pessoa.nome}for i in atividades]
        atividades.status()
        return response

    def post(self):
        dados = request.json
        pessoa = Pessoas.query.filter_by(nome=dados['pessoa']).first()
        atividade = Atividades(nome=dados['nome'], pessoa=pessoa)
        atividade.save()
        response = {
            'pessoa': atividade.pessoa.nome,
            'nome': atividade.nome,
            'id': atividade.id,
        }
        atividade.status()
        return response


class ListaAtividadesPessoas(Resource):
    def get(self, pessoa):
        atividades = Atividades.query.filter_by(pessoa=pessoa)
        try:
            response = [{'id': i.id, 'nome': i.nome, 'pessoa': i.pessoa.nome} for i in atividades]
            atividades.status()
        except AttributeError:
            response = {
                'status': 'error',
                'mensagem': f'Nenhuma tarefa para {pessoa} encontrada'
            }
        return response


api.add_resource(Pessoa, '/pessoa/<string:nome>/')
api.add_resource(ListaPessoas, '/pessoa/')
api.add_resource(ListaAtividades, '/atividades/')
api.add_resource(ListaAtividadesPessoas, '/atividades/<string:pessoa>/')
api.add_resource(Atividade, '/atividades/<int:id>/')
if __name__ == '__main__':
    app.run(debug=True)
