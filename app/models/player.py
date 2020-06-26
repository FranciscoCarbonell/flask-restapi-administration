from app import db, ms


class Player(db.Model):
    __tablename__ = 'player'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25))
    last_name = db.Column(db.String(50))
    position = db.Column(db.String(100), nullable=False)
    height = db.Column(db.Float(5), nullable=False)
    weight = db.Column(db.Float(5), nullable=False)
    image = db.Column(db.Unicode(255), nullable=False)
    image_name = db.Column(db.Unicode(255), nullable=False)

    def __repr__(self):
        return self.name


class SerializerPLayer(ms.ModelSchema):
    class Meta:
        model = Player