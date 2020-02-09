'''Questão 4
Na Samba, lidamos diariamente com um volume enorme de vídeos dos mais variados clientes.
Em nossa arquitetura estes vídeos são chamados de mídias.
Nessa questão, você deve fazer uma pequena aplicação capaz de receber, armazenar, listar e
buscar mídias. Uma mídia tem os seguinte atributos:
● Id (Integer)
    ○ Não pode ser nulo
    ○ Valor único
    ○ Valor: 0 < n < 10^7
● Nome (String)
    ○ Não pode ser nula
    ○ Até 512 caracteres
● URL (String)
    ○ Até 512 caracteres
● Duracao (Integer)
    ○ Valor: 0< n < 10^7
Os endpoints desta aplicação devem ser:
/medias POST (criar mídia)
/medias GET (listar mídias)
/medias/{id} GET (retornar uma mídia específica)
As mídias criadas na requisição POST devem ser mantidas de alguma maneira, de forma que
possam ser listadas e retornadas nas requisições GET. Para isso utilize qualquer método que
achar melhor.
'''

from flask import Flask, request, jsonify, render_template
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps

db_connect = create_engine('sqlite:///midias.db')
app = Flask(__name__)
api = Api(app)

class Midia(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute('select * from midia')
        result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
        return jsonify(result)

    def post(self):
        conn = db_connect.connect()
        nome = request.json['nome']
        url = request.json['url']
        duracao = request.json['duracao']

        conn.execute(
            "insert into midia values(null, '{0}', '{1}', '{2}')".format(nome, url, duracao)
        )

        query = conn.execute('select * from midia order by id')
        result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
        return jsonify(result)

    def put(self):
        conn = db_connect.connect()
        id = request.json['id']
        nome = request.json['nome']
        duracao = request.json['duracao']
        url = request.json['url']

        conn.execute(
            "update midia set "
            "nome = '" + str(nome) +"', "
            "duracao = '" + str(duracao) +"', "
            "url = '" + str(url) +"' "
            "where id =%d " %int(id)
        )

        query = conn.execute("select * from midia where id=%d " % int(id))
        result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
        return jsonify(result)

class MidiasById(Resource):
    def delete(self, id):
        conn = db_connect.connect()
        conn.execute("delete from midia where id=%d " %int(id))
        return{"status": "success"}

    def get(self, id):
        conn = db_connect.connect()
        query = conn.execute("select * from midia where id=%d " %int(id))
        result = [dict(zip(tuple(query.keys()), i)) for i in query.cursor]
        return jsonify(result)


api.add_resource(Midia, '/midias')
api.add_resource(MidiasById, '/midias/<id>')

if __name__ == '__main__':
    app.run()