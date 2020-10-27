# -*- coding: utf-8 -*-

from odoo import models, fields, api

class StockPicking(models.Model):
    _inherit = 'stock.picking'


    @api.multi
    def action_state_change(self):
        stock_move=self.env["stock.move"].search([('picking_id','=',self.id)],limit=1)
        stock_move.write({'state': 'draft'})
        stock_move_line = self.env["stock.move.line"].search([('picking_id', '=', self.id)], limit=1)
        return self.write({'state': 'draft'})
