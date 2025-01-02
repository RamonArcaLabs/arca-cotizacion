# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class QuotationImgOptions(models.Model):
    _name = 'quotation.img.options'
    _description = 'Arca Quotation Img Options'

    name = fields.Char(string='Nombre')
    image = fields.Image(string='Imagen')
