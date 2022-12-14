from concurrent.futures.process import _python_exit
from db import db 
from sqlalchemy.dialects.postgresql import UUID
import uuid
from flask_marshmallow import Marshmallow
import marshmallow as ma




class PetType(db.Model):
  __tablename__ = 'PetType'
  pet_id = db.Column(db.String(), primary_key=True, nullable=False)
  pet_type = db.Column(db.String(), nullable=False)
  breed_species = db.Column(db.String(), nullable=False)
  size = db.Column(db.String(), nullable=False)
  weight = db.Column(db.String(), nullable=False)
  temperment = db.Column(db.String(), nullable=False)
  active = db.Column(db.Boolean(), default=False, nullable=False)


  def __init__(self, pet_id, pet_type, breed_species, size, weight, temperment, active):
    self.pet_id = pet_id
    self.pet_type = pet_type
    self.breed_species = breed_species
    self.size = size
    self.weight = weight
    self.temperment = temperment
    self.active = active


class PetTypeSchema(ma.Schema):
  class Meta:
    fields = ['pet_id', 'pet_type', 'breed_species', 'size', 'weight', 'temperment', 'active', 'pet_info']

pet_type_schema = PetTypeSchema()
pets_type_schema = PetTypeSchema(many=True)