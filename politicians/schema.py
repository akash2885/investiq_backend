from ninja import ModelSchema, Schema
from .models import Politician


class PoliticianSchema(ModelSchema):
    class Meta:
        model = Politician
        fields = '__all__'


class PoliticianCreateSchema(Schema):
    firstName : str
    lastName : str
    transaction : str
    stock : str
    filed : str
    traded : str