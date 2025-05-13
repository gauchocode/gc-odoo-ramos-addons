from odoo import models, fields

class ProductPricelist(models.Model):
    _inherit = 'product.pricelist'

    journal_ids = fields.Many2many(
        comodel_name='account.journal',
        relation='product_pricelist_account_journal_rel',
        column1='pricelist_id',
        column2='journal_id',
        string='Journals'
    )