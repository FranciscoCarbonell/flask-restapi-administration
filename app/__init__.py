from flask import Flask
#from flask_cors import CORS
from flask_admin import Admin
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_marshmallow import Marshmallow
from flask_restplus import Api
from flask_login import LoginManager
from app.admin.admin_view import AdminView
from flask_uploads import configure_uploads

#cors = CORS(resources={r'/res_api/*': {"origins": "*"}})
admins = Admin(index_view=AdminView())
db = SQLAlchemy()
jwt = JWTManager()
ms = Marshmallow()
api = Api(doc='/doc')
login_manager = LoginManager()


def create_app(class_config='config.Developement'):
    app = Flask(__name__)
    app.config.from_object(class_config)

    #cors.init_app(app)
    db.init_app(app)
    jwt.init_app(app)
    ms.init_app(app)
    api.init_app(app)
    login_manager.init_app(app)
    admins.init_app(app)

    from app.login import bp_login
    from app.upload import bp_upload, photos
    #from app.res_api import auth
    from app.admin import admin
    from app import res_api

    app.register_blueprint(bp_login)
    app.register_blueprint(bp_upload)
    configure_uploads(app, photos)

    return app