from logging import getLogger

from flask import request
from flask_restplus import Resource, Namespace, Api


class ComResource(Resource):
    logger = getLogger('app.resource')

    def get_url_path(self, ns: Namespace):
        _api: Api = self.api
        base_url: str = '{base_path}{ns_path}'.format(base_path=_api.base_path[:-1], ns_path=_api.get_ns_path(ns))
        return request.path.replace(base_url, '')

    def __init__(self, *args, **kwargs):
        super(ComResource, self).__init__(*args, **kwargs)
