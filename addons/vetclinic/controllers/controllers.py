# -*- coding: utf-8 -*-
from odoo import http

# class Vetclinic(http.Controller):
#     @http.route('/vetclinic/vetclinic/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vetclinic/vetclinic/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('vetclinic.listing', {
#             'root': '/vetclinic/vetclinic',
#             'objects': http.request.env['vetclinic.vetclinic'].search([]),
#         })

#     @http.route('/vetclinic/vetclinic/objects/<model("vetclinic.vetclinic"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vetclinic.object', {
#             'object': obj
#         })