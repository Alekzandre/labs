from .. import db


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_intra = db.Column(db.Integer, unique=False, index=True)
    name = db.Column(db.String(64), unique=True, index=True)
    desc = db.Column(db.String(512))
