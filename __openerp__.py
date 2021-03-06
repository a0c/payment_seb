# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2015 AVANSER LLC (<http://avanser.ee>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'SEB Banklink',
    'author': 'Anton Chepurov @ AVANSER LLC',
    'version': '1.0',
    'category': 'Hidden',
    'summary': 'Payment Acquirer: SEB Banklink Implementation',
    'description': """
SEB Banklink
============
Implements SEB banklink ('pangalink') used in Estonia.
""",
    'website': 'www.avanser.ee',
    'depends': ['payment_banklink'],
    'data': [
        'views/seb_template.xml',
        'views/seb_view.xml',
        'data/seb.xml',
    ],
}
