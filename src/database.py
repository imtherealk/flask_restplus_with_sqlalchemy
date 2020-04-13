"""
database
========

Utilities for database.

"""
import sqlalchemy as s
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class IDPKMixin(object):
    """General PK mixin."""
    id = db.Column(db.Integer, primary_key=True)


class DescriptionMixin(object):
    description = db.Column(db.TEXT)


class SystemMixin(object):
    """General creation-time mixin."""
    created_at = db.Column(db.TIMESTAMP(timezone=True), nullable=False, default=s.func.now())
    created_by = db.Column(db.TEXT)
    updated_at = db.Column(db.TIMESTAMP(timezone=True))
    updated_by = db.Column(db.TEXT)
    deleted_at = db.Column(db.TIMESTAMP(timezone=True))
    deleted_by = db.Column(db.TEXT)
    is_deleted = db.Column(db.BOOLEAN, nullable=False, default=0)

