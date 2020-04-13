from flask import Blueprint
from flask_restplus import Api

from api.resource.site_resource import site_ns

_API_NAME = 'v1'
_API_ROOT_PATH = '/api/' + _API_NAME

blueprint = Blueprint(_API_NAME, __name__, url_prefix=_API_ROOT_PATH)

api = Api(
    blueprint,
    title='Sample API',
    version='1.0',
    description='API for flask_restplus_with_sqlalchemy',
    doc='/',
)

api.add_namespace(site_ns, path='/sites')
