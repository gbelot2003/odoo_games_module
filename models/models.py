# -*- coding: utf-8 -*-

from odoo import models, fields, api
class games_register(models.Model):
     _name = 'games_register.manager'
     _description = "Registro maestro de juegos"

     name = fields.Char(string = "Nombre del Juego", required = True)
     value = fields.Integer()
     description = fields.Text()
     responsable_id = fields.Many2one('res.users', ondelete='set null', string="responsable", index=True)
     tags_id = fields.Many2one('games_register.tags', ondelete='cascade', string="tags", index=True)


class tags(models.Model):
     _name = 'games_register.tags'
     _description = "Un Tag de clasificación para cada juego"

     name = fields.Char(string="Nombre Tag", required=True)
     description = fields.Text()
     games_ids = fields.One2many('games_register.manager', 'tags_id', string='Juegos')


#     value2 = fields.Float(compute="_value_pc", store=True)

#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100