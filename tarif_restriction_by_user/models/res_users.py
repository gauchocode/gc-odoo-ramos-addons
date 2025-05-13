from odoo import models, fields

class ResUsers(models.Model):
    _inherit = 'res.users'

    pricelist_ids = fields.Many2many(
        comodel_name='product.pricelist',
        relation='res_users_pricelist_rel',
        column1='user_id',
        column2='pricelist_id',
        string='Allowed Pricelists'
    )

    default_pricelist_id = fields.Many2one(
        comodel_name='product.pricelist',
        string='Default Pricelist'
    )