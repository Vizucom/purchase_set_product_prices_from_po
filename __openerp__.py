# -*- coding: utf-8 -*-
##############################################################################
#
#   Copyright (c) 2016- Vizucom Oy (http://www.vizucom.com)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Update Cost Prices from PO',
    'category': 'Purchase',
    'version': '0.1',
    'author': 'Vizucom Oy',
    'website': 'http://www.vizucom.com',
    'depends': ['purchase'],
    'description': """
Update Cost Prices from PO
==========================
 * Adds the possibility to batch update products' cost prices from Purchase Order, based on the prices set on PO lines

""",
    'data': [
        'views/purchase_order.xml',
    ]
}
