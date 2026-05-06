from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bank.db'
db = SQLAlchemy(app)

class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    balance = db.Column(db.Float)

def transfer(from_id, to_id, amount):
    try:
        sender = Account.query.get(from_id)
        receiver = Account.query.get(to_id)

        sender.balance -= amount
        receiver.balance += amount

        db.session.commit()
        print("Transfer success")

    except:
        db.session.rollback()
        print("Transfer failed")

with app.app_context():
    db.create_all()

    a1 = Account(balance=1000)
    a2 = Account(balance=500)

    db.session.add_all([a1, a2])
    db.session.commit()

    transfer(1, 2, 200)
