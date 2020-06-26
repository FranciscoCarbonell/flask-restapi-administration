from flask import Flask
from app import db
from flask_migrate import Migrate, MigrateCommand, Manager
from app.models.player import Player
from app.models.user import User, UserRoles

app = Flask(__name__)
app.config.from_object("config.Manager")

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command("db", MigrateCommand)

if __name__ == "__main__":
    manager.run()