from db import db

class UserData(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(9))
    date_of_birth = db.Column(db.String(59))
    username = db.Column(db.String(13))
    password = db.Column(db.String(13))
    email = db.Column(db.String(40))

    def __init__(self,name, date_of_birth,username,password,email):
        self.name = name
        self.date_of_birth = date_of_birth
        self.username = username
        self.password = password
        self.email = email
    def json(self):
        return {'name': self.name , 'date_of_birth':self.date_of_birth, 'username':self.username
        ,'password':self.password,'email':self.email}
    def save_to_db(self,):
        db.session.add(self)
        db.session.commit()
    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_password(cls, password):
        return cls.query.filter_by(password=password).first()


    @classmethod
    def find_by_email(cls,email):
        return cls.query.filter_by(email=email).first()
    @classmethod
    def find_by_id(cls ,id):
        return cls.query.filter_by(id=id).first()
