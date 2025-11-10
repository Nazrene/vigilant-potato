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
    name = db.Column(db.String(100), nullable=False, index=True)
    ingredients = db.Column(db.Text, nullable=False)
    instructions = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(1024), nullable=True)
    user_id = db.Column(db.Integer, db.Foreignkey("users.id"), nullable=False, index=True)

    author = db.Relationship("User", back_populates="recipes")
    reviews = db.Relationship("Review", back_populates="recipe", cascade="all, delete-orphan")

class Review(db.Model):
    __tablename__ = "reviews"
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False, index=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey("recipes.id"), nullable=False, index=True)

    author = db.Relationship("User", back_populates="reviews")
    recipe = db.Relationship("Recipe", back_populates="review")


    def __repr__(self):
        return f"<Recipe {self.name}>"