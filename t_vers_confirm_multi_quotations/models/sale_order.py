# -*- coding: utf-8 -*-
from odoo import models

class SaleOrder(models.Model):
    _inherit = "sale.order"

    def action_confirm_selected_quotations(self):
        for order in self:
            if order.state in ("draft", "sent"):
                order.action_confirm()
