from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from datetime import datetime
import logging
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)

# CONNECT TO DATABASE CONFIG
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:<password>@localhost/derso_db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
db.init_app(app)
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

# FILES
app.config["USER_IMAGE_UPLOADS"] = 'files/user_images'
