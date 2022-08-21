from flask import Flask, render_template
import json
from flask import flash, redirect
from database import db
from flask_migrate import Migrate
from models import Usuario
from usuarios import bp_usuarios


app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'
app.register_blueprint(bp_usuarios, url_prefix='/usuarios')

conexao = "sqlite:///meubanco.db"
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def index():
    return 'Hello, from Flask!'

@app.route("/teste_insert")
def teste_insert():
    u = Usuario("Alba Lopes", "albasandyra@gmail.com", "123456")
    db.session.add(u)
    db.session.commit()
    return 'Dados inseridos com sucesso'

@app.route("/teste_select")
def teste_select():
    u = Usuario.query.all()
		#esse código de print vai aparecer no terminal, não no navegador
    print(u)
    u = Usuario.query.get(1)
		#já esse return é que vai aparecer no navegador
    return u.nome

@app.route("/teste_update")
def teste_update():
    u = Usuario.query.get(1)  
    u.nome = "Alba L."
    db.session.add(u)
    db.session.commit()
    return 'Dados atualizados com sucesso'

@app.route("/teste_delete")
def teste_delete():		
    u = Usuario.query.get(1)
    db.session.delete(u)
    db.session.commit()
    return 'Dados excluídos com sucesso'

app.run(host='0.0.0.0', port=81)