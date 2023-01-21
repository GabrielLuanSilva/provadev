import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

BASEDIR = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(BASEDIR, 'database.db')
db = SQLAlchemy(app)


class Estado(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    cidades = db.relationship('Cidade', backref='cidades', lazy=True)

    def __repr__(self):
        return str({'id': self.id, 'nome': self.nome, 'cidades': self.cidades})


class Cidade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    bairros = db.relationship('Bairro', backref='bairro', lazy=True)
    estado_id = db.Column(db.Integer, db.ForeignKey('estado.id'), nullable=False)

    def __repr__(self):
        return str({'id': self.id, 'nome': self.nome, 'bairros': self.bairros, 'estado': self.estado_id})


class Bairro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    cidade_id = db.Column(db.Integer, db.ForeignKey('cidade.id'), nullable=False)

    def __repr__(self):
        return str({'id': self.id, 'nome': self.nome, 'cidade_id': self.cidade_id})


with app.app_context():
    db.drop_all()
    db.create_all()
    db.session.add_all([
        Estado(id=1, nome="Paraná"),
        Estado(id=2, nome="Goiás"),

        Cidade(id=1, nome='Noronha', estado_id=1),
        Cidade(id=2, nome='Diamantina', estado_id=2),

        Bairro(id=1, nome="Agostinho", cidade_id=1),
        Bairro(id=2, nome="Natal", cidade_id=1),
        Bairro(id=3, nome="Betânia", cidade_id=1),
    ])
    db.session.commit()

    estados = db.session.execute(db.select(Estado)).all()
    for estado in estados:
        print(estado[0])

    cidades = db.session.execute(db.select(Cidade)).all()
    for cidade in cidades:
        print(cidade[0])

    bairros = db.session.execute(db.select(Bairro)).all()
    for bairro in bairros:
        print(bairro[0])
