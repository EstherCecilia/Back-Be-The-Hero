from flask import Flask, request
from flask_restful import Resource, Api
import json
from models import *

app = Flask(__name__)
api = Api(app)



class Tarefas(Resource):
    def get(self):
        dados = request.json
        tarefa = Tarefa.query.filter_by(usuario=dados['id']).all()
        try:
            response = {'status': True, 'tarefas':[{'id':i.id, 'titulo':i.titulo, 'descricao': i.descricao, 'tempo':i.tempo} for i in tarefa]}
            

        except AttributeError:
            response = {'status': False}
            
        return response

    def post(self):
        dados = request.json
        tarefa = Tarefa(titulo=dados['titulo'], descricao=dados['descricao'], tempo=dados['tempo'], usuario=dados['usuario'])
        tarefa.save()
        response = {
            'status':True,
            'id' : tarefa.id
            }

        return response
    
    
    def delete(self):
        dados = request.json
        tarefa = Tarefa.query.filter_by(id=dados['id']).first()

        try:
            tarefa.delete()
            reponse = {'status': True, 'mensagem': 'Registro excluido'}

        except AttributeError:
            response = {'status': False}

        return response


class Usuarios(Resource):
    def get(self):
        dados = request.json
        usuario = Usuario.query.filter_by(id=dados['id']).first()
        try:
            response = {'status': True, 'id':usuario.id, 'nome':usuario.nome}
            
        except AttributeError:
            response = {'status': False}
            
        return response
    
    def post(self):
        dados = request.json
        usuario = Usuario(nome=dados['nome'], email=dados['email'])
        usuario.save()
        response = {
            'status':True,
            'id' : usuario.id,
            'nome' : usuario.nome
            }

        return response


api.add_resource(Tarefas, '/tarefa')
api.add_resource(Usuarios, '/usuario')

if __name__ == '__main__':
    app.run(debug=True)

