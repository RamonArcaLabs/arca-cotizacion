# -*- coding: utf-8 -*-

from odoo import models, fields

class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    arca_concept = fields.Html(string="Concepto")