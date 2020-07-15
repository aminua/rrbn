# -*- coding: utf-8 -*-
from odoo import http

# class TreasuryBooks(http.Controller):
#     @http.route('/treasury_books/treasury_books/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/treasury_books/treasury_books/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('treasury_books.listing', {
#             'root': '/treasury_books/treasury_books',
#             'objects': http.request.env['treasury_books.treasury_books'].search([]),
#         })

#     @http.route('/treasury_books/treasury_books/objects/<model("treasury_books.treasury_books"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('treasury_books.object', {
#             'object': obj
#         })