from odoo import models

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def _prepare_invoice(self):
        invoice_vals = super()._prepare_invoice()

        # Establecer la orden de venta asociada
        invoice_vals['sale_order_id'] = self.id

        # Obtener diarios permitidos desde la tarifa
        journal_ids = self.pricelist_id.journal_ids.ids
        if journal_ids:
            invoice_vals['journal_id'] = journal_ids[0]  # Elegimos el primero
        else:
            # Opcional: no establecer nada si no hay diarios definidos
            invoice_vals.pop('journal_id', None)

        return invoice_vals

    def action_create_invoice(self):
        action = super().action_create_invoice()

        if len(self) != 1:
            return action  # solo para una sola orden

        invoice = self.invoice_ids.filtered(lambda inv: inv.state == 'draft')[:1]
        if not invoice:
            return action

        # Buscar los diarios válidos desde la tarifa
        journal_ids = self.pricelist_id.journal_ids.ids
        if not journal_ids:
            raise UserError("La tarifa no tiene diarios asociados. No se puede crear la factura.")

        # Modificar el context de la acción para establecer dominio de journal_id
        action['context'] = dict(action.get('context', {}))
        action['context'].update({
            'default_sale_order_id': self.id,
            'default_journal_id': journal_ids[0],
            'journal_id_domain': [('id', 'in', journal_ids)],
        })
        
        return action
