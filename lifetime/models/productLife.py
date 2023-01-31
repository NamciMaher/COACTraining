from datetime import datetime

from odoo import api, fields, models


class Product(models.Model):
    _inherit = 'product.template'

    date_receipt = fields.Datetime(string='Receipt Date')
    lifetime = fields.Float(string='Lifetime', compute='_compute_lifetime')

    @api.depends('date_receipt')
    def _compute_lifetime(self):
        for product in self:
            if product.date_receipt:
                dt1 = fields.Datetime.from_string(product.date_receipt)
                dt2 = datetime.now()
                delta = dt2 - dt1
                product.lifetime = delta.total_seconds() / (3600 * 24)
            else:
                product.lifetime = 0.0
