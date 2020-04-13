import sqlalchemy as s
from flask import make_response
from flask_restplus import Namespace
from sqlalchemy.exc import IntegrityError

from api.com_resource import ComResource
from api.form.site_form import SiteCreateForm, SiteUpdateForm
from api.schema.site_schema import SiteSchema
from api.service.site_service import SiteService
from api.model.site_model import Site
from database import db
from serializer import render, FormSchema

site_ns = Namespace('site', description='Site API')

parser = site_ns.parser()
parser.add_argument('name', type=str, help='site name', location='form')
parser.add_argument('code', type=str, help='site code', location='form')
parser.add_argument('created_by', type=str, help='user value', location='form')
parser.add_argument('updated_by', type=str, help='user value', location='form')


@site_ns.route('/')
class SiteGetAllResource(ComResource):
    site_service: SiteService = SiteService()

    def get(self):
        """Get All Sites"""
        sites = Site.query.filter_by(is_deleted=False).order_by(Site.created_at).paginate()
        return make_response(render(data=sites, schema=SiteSchema, many=True), 200)

    @site_ns.doc(parser=parser)
    def post(self):
        """Create A Site"""
        form = SiteCreateForm()

        if form.validate_on_submit():
            site = Site(
                name=form.name.data,
                code=form.code.data,
                created_by=form.created_by.data
            )
            db.session.add(site)
            try:
                db.session.commit()
                return make_response(render(data=site, schema=SiteSchema), 201)
            except IntegrityError as e:
                db.session.rollback()
                return make_response(render(form, FormSchema, e.args), 400)
        return make_response(render(form, FormSchema), 400)


@site_ns.route('/<int:id>')
class SiteGetResource(ComResource):
    site_service: SiteService = SiteService()

    def get(self, id):
        """Get A Site by id"""
        site = Site.query.get(id)

        return make_response(render(data=site, schema=SiteSchema), 200)

    @site_ns.doc(parser=parser)
    def put(self, id):
        """Update A Site by id"""
        site = Site.query.get(id)
        form = SiteUpdateForm()
        if form.validate_on_submit():
            site.name = form.name.data
            site.created_by = form.created_by.data
            site.updated_by = form.updated_by.data
            site.updated_at = s.func.now()
            db.session.commit()
            return make_response(render(data=site, schema=SiteSchema), 200)
        return make_response(render(form, FormSchema), 400)

    def delete(self, id):
        """Delete A Site by id"""
        site = Site.query.get(id)
        site.is_deleted = True
        site.updated_at = s.func.now()
        site.deleted_at = s.func.now()
        db.session.commit()
        return make_response(render(None), 200)
