from db import db

class PersonModel(db.Model):
    __tablename__ = 'person'

    id = db.Column(db.Integer, primary_key=True)
    person_name = db.Column(db.String(80))
    phone_number = db.Column(db.String(80))

    def __init__(self, person_name, phone_number):
        self.person_name = person_name
        self.phone_number = phone_number

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_name(cls, person_name):
        return cls.query.filter_by(person_name=person_name).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()