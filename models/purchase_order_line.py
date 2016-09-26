# -*- coding: utf-8 -*-
from openerp.osv import osv, fields
from openerp.tools.translate import _

class PurchaseOrderLine(osv.Model):

    _inherit = 'purchase.order.line'

    _columns = {
        'update_price': fields.boolean('Update Cost Price', help='''Checked lines' products will have their Cost Prices updated according to the price on the line when Purchase Order's 'Update Prices' button is clicked. ''')
    }
