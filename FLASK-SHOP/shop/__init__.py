from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


app = Flask(__name__)

app.config['SECRET_KEY'] = 'd1be60c7665e5b97cedeb20978baece1445750123cec59d0'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://c1964235:vamosVAM123@csmysql.cs.cf.ac.uk:3306/c1964235_ECOM'
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

from shop import routes
