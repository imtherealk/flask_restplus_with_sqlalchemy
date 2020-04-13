"""
serializer
==========

Utils for serialization

"""
from flask import jsonify
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import Pagination
from marshmallow import fields

ma = Marshmallow()


class DictField(fields.Field):
    """Typed dict field."""
    def __init__(self, key_field, nested_field, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.key_field = key_field
        self.nested_field = nested_field

    def _deserialize(self, value, **kwargs):
        ret = {}
        for key, val in value.items():
            k = self.key_field.deserialize(key)
            v = self.nested_field.deserialize(val)
            ret[k] = v
        return ret

    def _serialize(self, value, attr, obj, **kwargs):
        ret = {}
        for key, val in value.items():
            k = self.key_field.serialize(attr, obj)
            v = self.nested_field.serialize(key, obj)
            ret[k] = v
        return ret


class FormSchema(ma.Schema):
    """Generic WTForms schema."""
    errors = DictField(fields.String(), fields.String())


def render(data, schema=None, metadata=None, *args, **kwargs):
    """
    Render value with schema.

    :param data: data to be serialized.
    :param schema: schema to be used in serialization.
    :param metadata: metadata to be sent with data.
    :param args: args to serialize method in schema.
    :param kwargs: kwargs to serialize method in schema.
    """
    metadata = metadata or {}

    if isinstance(data, Pagination):
        pagination = data
        data = pagination.items
        metadata.update({
            'page': pagination.page,
            'per_page': pagination.per_page,
            'total': pagination.total,
        })
    if schema:
        data = schema().dump(data, *args, **kwargs)

    result = {
        'data': data,
        'metadata': metadata,
    }

    return jsonify(result)
