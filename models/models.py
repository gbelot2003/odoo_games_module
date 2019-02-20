# -*- coding: utf-8 -*-

from odoo import models, fields, api
class games_register(models.Model):
     _name = 'games_register.manager'
     _description = "Registro maestro de juegos"

     name = fields.Char(string = "Nombre del Juego", required = True)
     value = fields.Integer()
     description = fields.Text()
#     value2 = fields.Float(compute="_value_pc", store=True)

#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100