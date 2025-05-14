from odoo import models, fields, api
from odoo.exceptions import ValidationError

class AccountMove(models.Model):
    _inherit = 'account.move'

    sale_order_id = fields.Many2one('sale.order', string='Sale Order')

    @api.depends('company_id', 'invoice_filter_type_domain', 'sale_order_id')
    def _compute_suitable_journal_ids(self):
        for m in self:
            journal_type = m.invoice_filter_type_domain or 'general'
            company_id = m.company_id.id or self.env.company.id

            domain = [
                ('company_id', '=', company_id),
                ('type', '=', journal_type),
            ]

            # Si hay sale_order_id con tarifa y diarios definidos, filtramos por eso
            if m.sale_order_id and m.sale_order_id.pricelist_id.journal_ids:
                journal_ids = m.sale_order_id.pricelist_id.journal_ids.ids
                domain.append(('id', 'in', journal_ids))

            m.suitable_journal_ids = self.env['account.journal'].search(domain)


    @api.constrains('sale_order_id', 'journal_id')
    def _check_journal_in_tarif(self):
        for move in self:
            if move.sale_order_id:
                allowed = move.sale_order_id.pricelist_id.journal_ids
                if move.journal_id and move.journal_id not in allowed:
                    raise ValidationError(
                        f"El diario '{move.journal_id.display_name}' no está permitido según la tarifa de la orden de venta."
                    )

    @api.onchange('sale_order_id')
    def _onchange_sale_order_id(self):
        if self.sale_order_id and self.sale_order_id.pricelist_id.journal_ids:
            journal_ids = self.sale_order_id.pricelist_id.journal_ids.ids
            return {
                'domain': {'journal_id': [('id', 'in', journal_ids)]}
            }
        else:
            return {
                'domain': {'journal_id': []}  # o no establecer dominio si querés permitir todos
            }
