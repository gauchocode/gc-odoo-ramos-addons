from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    allowed_pricelist_ids = fields.Many2many(
        comodel_name='product.pricelist',
        compute='_compute_allowed_pricelist_ids',
        string='Allowed Pricelists'
    )

    @api.depends('user_id')
    def _compute_allowed_pricelist_ids(self):
        for order in self:
            order.allowed_pricelist_ids = self.env.user.pricelist_ids
