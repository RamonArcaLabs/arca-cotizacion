# -*- coding: utf-8 -*-

from odoo import models, fields

class SaleOrderTemplate(models.Model):
    _inherit = "sale.order.template"

    arca_introduccion = fields.Html(string='Introducción')
    arca_alcance_del_proyecto = fields.Html(string='Alcance del Proyecto')
    arca_alcance_organizacional = fields.Html(string='Alcance Organizacional')
    arca_metodologia = fields.Html(string='Metodología')
    arca_alcance_tecnico_y_fases = fields.Html(string='Alcance Técnico y Fases')
    arca_condiciones_generales_y_terminos = fields.Html(string='Condiciones Generales y Términos')

