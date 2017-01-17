# -*- coding: utf-8 -*-
##############################################################################
#
#    Product - Average Consumption Module for Odoo
#    Copyright (C) 2013-Today GRAP (http://www.grap.coop)
#    @author Julien WESTE
#    @author Sylvain LE GAL (https://twitter.com/legalsylvain)
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

from openerp import api, models


class ProductProduct(models.Model):
    _inherit = "product.product"

# Column section
    @api.model
    def correct_history(self):
        histories = self.env['product.history'].search([
            ('from_date', '>=', '2016-12-12')])
        histories.unlink()
        products = self.env['product.product'].search([
            '|', ('active', '=', True),
            ('active', '=', False)])
        for product in products:
            product.with_context(
                prefetch_fields=False)._compute_history('months')
            product.with_context(
                prefetch_fields=False)._compute_history('weeks')
            # product._compute_history('days')