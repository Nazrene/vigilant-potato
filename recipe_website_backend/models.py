from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__= "users"

    id = db.Column(db.Integer , primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(255) , nullable=False , unique=True, index=True)
    password_hash = db.Column(db.String(255), nullable=False)

    recipes = db.relationship("Recipe", back_populates="author", cascade="all, delete-orphan")
    reviews = db.relationship("Review", back_populates="author", cascade="all, delete-orphan")

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    ingredients = db.Column(db.Text, nullable=False)
    instructions = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"<Recipe {self.name}>"