from .. import db

class Contrat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True)
    slot = db.Column(db.Integer)
    used_slot = db.Column(db.Integer, default=0)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
    firm_id = db.Column(db.Integer, db.ForeignKey('firm.id'))