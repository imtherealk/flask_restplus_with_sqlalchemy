from database import db, IDPKMixin, DescriptionMixin, SystemMixin


class Site(db.Model, IDPKMixin, DescriptionMixin, SystemMixin):
    """Site model"""
    __tablename__ = 'site'

    name = db.Column(db.Text)
    code = db.Column(db.Text, unique=True)
