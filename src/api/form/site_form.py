from wtforms import fields, validators as v

from base import Form


class SiteCreateForm(Form):
    """Site 등록 form"""
    name = fields.StringField('Name', [v.data_required()])
    code = fields.StringField('Code', [v.data_required()])
    created_by = fields.StringField('User', [v.data_required()])


class SiteUpdateForm(Form):
    """Site 수정 form"""
    name = fields.StringField('Name')
    created_by = fields.StringField('User')
    updated_by = fields.StringField('User')
