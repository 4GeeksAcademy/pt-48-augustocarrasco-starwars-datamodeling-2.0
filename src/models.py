from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return "<User %r>" % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }


class Item(db.Model):
    __tablename__ = "items"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    img = db.Column(db.String(), unique=True, nullable=False)
    description = db.Column(db.String(), unique=True, nullable=False)

    characters = db.relationship("Character", back_populates="items")
    planets = db.relationship("Planet", back_populates="items")
    starships = db.relationship("Starship", back_populates="items")

    def __repr__(self):
        return "<Item %r>" % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "img": self.img,
            "description": self.description,
        }


class Character(db.Model):
    __tablename__ = "characters"
    item = db.Column(db.Integer, db.ForeignKey("items.id"))
    id = db.Column(db.Integer, primary_key=True)
    height = db.Column(db.Integer, nullable=False)
    mass = db.Column(db.Integer, nullable=False)
    hair_color = db.Column(db.String, nullable=False)
    skin_color = db.Column(db.String, nullable=False)
    eye_color = db.Column(db.String, nullable=False)
    birth_year = db.Column(db.String, nullable=False)
    gender = db.Column(db.String, nullable=False)
    created = db.Column(db.String, nullable=False)
    edited = db.Column(db.String, nullable=False)
    homeworld = db.Column(db.String, nullable=False)

    items = db.relationship("Item", back_populates="characters")
    def __repr__(self):
        return "<Character >"

    def serialize(self):
        return {
            "height": self.height,
            "mass": self.mass,
            "hair_color": self.hair_color,
            "skin_color": self.skin_color,
            "eye_color": self.eye_color,
            "birth_year": self.birth_year,
            "gender": self.gender,
            "created": self.created,
            "edited": self.edited,
            "homeworld": self.homeworld,
        }


class Planet(db.Model):
    __tablename__ = "planets"
    item = db.Column(db.Integer, db.ForeignKey("items.id"))
    id = db.Column(db.Integer, primary_key=True)
    diameter = db.Column(db.String, nullable=False)
    rotation_period = db.Column(db.Integer, nullable=False)
    orbital_period = db.Column(db.Integer, nullable=False)
    gravity = db.Column(db.String, nullable=False)
    population = db.Column(db.Integer, nullable=False)
    climate = db.Column(db.String, nullable=False)
    terrain = db.Column(db.String, nullable=False)
    surface_water = db.Column(db.Boolean, nullable=False)
    created = db.Column(db.String, nullable=False)
    edited = db.Column(db.String, nullable=False)

    items = db.relationship("Item", back_populates="planets")

    def __repr__(self):
        return "<Planet >"

    def serialize(self):
        return {
            "diameter": self.diameter,
            "rotation_period": self.rotation_period,
            "orbital_period": self.orbital_period,
            "gravity": self.gravity,
            "population": self.population,
            "climate": self.climate,
            "terrain": self.terrain,
            "surface_water": self.surface_water,
            "created": self.created,
            "edited": self.edited,
        }


class Starship(db.Model):
    __tablename__ = "starships"
    item = db.Column(db.Integer, db.ForeignKey("items.id"))
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String, nullable=False)
    starship_class = db.Column(db.String, nullable=False)
    cost_in_credits = db.Column(db.Integer, nullable=False)
    length = db.Column(db.Integer, nullable=False)
    crew = db.Column(db.Integer, nullable=False)
    passengers = db.Column(db.Integer, nullable=False)
    max_atmosphere_speed = db.Column(db.Integer, nullable=False)
    hyperdrive_rating = db.Column(db.String, nullable=False)
    MGLT = db.Column(db.Integer, nullable=False)
    cargo_capacity = db.Column(db.Integer, nullable=False)
    consumables = db.Column(db.String, nullable=False)
    created = db.Column(db.String, nullable=False)
    edited = db.Column(db.String, nullable=False)

    items = db.relationship("Item", back_populates="starships")

    def __repr__(self):
        return "<Starship >"

    def serialize(self):
        return {
            "model": self.model,
            "starship_class": self.starship_class,
            "cost_in_credits": self.cost_in_credits,
            "length": self.length,
            "crew": self.crew,
            "passengers": self.passengers,
            "max_atmosphere_speed": self.max_atmosphere_speed,
            "hyperdrive_rating": self.hyperdrive_rating,
            "MGLT": self.MGLT,
            "cargo_capacity": self.cargo_capacity,
            "consumables": self.consumables,
            "created": self.created,
            "edited": self.edited,
        }
