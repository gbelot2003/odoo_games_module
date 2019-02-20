# -*- coding: utf-8 -*-
from odoo import http

# class GamesRegister(http.Controller):
#     @http.route('/games_register/games_register/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/games_register/games_register/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('games_register.listing', {
#             'root': '/games_register/games_register',
#             'objects': http.request.env['games_register.games_register'].search([]),
#         })

#     @http.route('/games_register/games_register/objects/<model("games_register.games_register"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('games_register.object', {
#             'object': obj
#         })