# -*- coding: utf-8 -*-
from openerp.osv import osv, fields
from openerp.tools.translate import _

class PurchaseOrder(osv.Model):

    _inherit = 'purchase.order'

    def set_cost_prices(self, cr, uid, ids, context=None):

        product_model = self.pool.get('product.product')

        for po_line in self.browse(cr, uid, ids[0], context).order_line:
            if po_line.update_price and po_line.product_id and po_line.price_unit:
                product_model.write(cr, uid, [po_line.product_id.id], {
                    'standard_price': po_line.price_unit
                })

        return {}
