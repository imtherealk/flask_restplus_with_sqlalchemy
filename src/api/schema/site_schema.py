"""

Site schemas for serialization

"""
from api.model.site_model import Site
from serializer import ma


class SiteSchema(ma.ModelSchema):
    class Meta:
        model = Site
        fields = ['id', 'name', 'code', 'is_deleted']
