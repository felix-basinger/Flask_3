from flask import Flask, render_template, request, redirect
from werkzeug.security import generate_password_hash
from models import db, Users

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.db'

db.init_app(app)


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # try:
        hash_psw = generate_password_hash(request.form['password'])
        name = request.form['first_name']
        users = Users(first_name=name,
                      last_name=request.form['last_name'],
                      email=request.form['email'],
                      password=hash_psw)
        db.session.add(users)
        db.session.commit()
        return render_template('hello.html', name=name)
        # except:
        #     db.session.rollback()
        #     print("Ошибка добавления в БД")
    else:
        return render_template("register.html")


@app.route('/hello', methods=["GET", "POST"])
def hello():
    return render_template('hello.html')
