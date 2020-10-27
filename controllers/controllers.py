# -*- coding: utf-8 -*-
from odoo import http

# class Extra-addons/methodStockPickinkStatusChange(http.Controller):
#     @http.route('/extra-addons/method_stock_pickink_status_change/extra-addons/method_stock_pickink_status_change/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/extra-addons/method_stock_pickink_status_change/extra-addons/method_stock_pickink_status_change/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('extra-addons/method_stock_pickink_status_change.listing', {
#             'root': '/extra-addons/method_stock_pickink_status_change/extra-addons/method_stock_pickink_status_change',
#             'objects': http.request.env['extra-addons/method_stock_pickink_status_change.extra-addons/method_stock_pickink_status_change'].search([]),
#         })

#     @http.route('/extra-addons/method_stock_pickink_status_change/extra-addons/method_stock_pickink_status_change/objects/<model("extra-addons/method_stock_pickink_status_change.extra-addons/method_stock_pickink_status_change"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('extra-addons/method_stock_pickink_status_change.object', {
#             'object': obj
#         })