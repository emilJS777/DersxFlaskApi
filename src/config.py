from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from datetime import datetime
import logging
from flask_cors import CORS
from flask_socketio import SocketIO
from flask_mail import Mail


app = Flask(__name__, static_folder='../files')
api = Api(app)
with app.app_context():
    # CONNECT TO DATABASE CONFIG
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:<password>@localhost/derso_db?charset=utf8mb4"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config['MYSQL_DATABASE_CHARSET'] = 'utf8mb4'
    db = SQLAlchemy()
    db.init_app(app) # Initialize the SQLAlchemy instance with the Flask app
    db.create_all()
    migrate = Migrate(app, db)

    # CONNECT JWT CONFIG
    app.config["JWT_SECRET_KEY"] = "Hs&67KCsn@77G"
    app.config["JWT_ACCESS_EXP"] = 60
    app.config["JWT_REFRESH_EXP"] = 3000
    app.config["JWT_ALGORITHM"] = "HS256"
    jwt = JWTManager(app)

    # LOGGING
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(f"{datetime.utcnow()}")

    # Set CORS options on app configuration
    app.config['CORS_RESOURCES'] = {r"/*": {"origins": "*"}}
    app.config['CORS_HEADERS'] = 'Content-Type'
    CORS(app, supports_credentials=True)

    # SOCKETIO
    socketio = SocketIO(app, cors_allowed_origins="*")

    # FILES
    app.config["USER_IMAGE_UPLOADS"] = 'files/user_images'
    app.config["SERVICE_IMAGE_UPLOADS"] = 'files/service_images'
    app.config["PUBLICATION_IMAGE_UPLOADS"] = 'files/publication_images'
    app.config["IMAGE_UPLOADS"] = 'files/images'
    app.config["LANGS"] = 'files/langs'

    # MAIL CONFIG
    app.config['MAIL_SERVER'] = 'smtp.mail.ru'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USERNAME'] = 'test-test-9292@mail.ru'
    app.config['MAIL_PASSWORD'] = 'nHzYGRmhSv41y5YE3VCD'
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True
    mail = Mail(app)

    # FRONT
    app.config['FRONT_LINK'] = 'http://127.0.0.1:80'

