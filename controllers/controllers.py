# -*- coding: utf-8 -*-
from odoo import http

# class Productos2(http.Controller):
#     @http.route('/productos2/productos2/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/productos2/productos2/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('productos2.listing', {
#             'root': '/productos2/productos2',
#             'objects': http.request.env['productos2.productos2'].search([]),
#         })

#     @http.route('/productos2/productos2/objects/<model("productos2.productos2"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('productos2.object', {
#             'object': obj
#         })