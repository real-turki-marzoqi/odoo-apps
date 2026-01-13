# -*- coding: utf-8 -*-
# from odoo import http


# class EraConfirmMultiQuotations(http.Controller):
#     @http.route('/era_confirm_multi_quotations/era_confirm_multi_quotations', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/era_confirm_multi_quotations/era_confirm_multi_quotations/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('era_confirm_multi_quotations.listing', {
#             'root': '/era_confirm_multi_quotations/era_confirm_multi_quotations',
#             'objects': http.request.env['era_confirm_multi_quotations.era_confirm_multi_quotations'].search([]),
#         })

#     @http.route('/era_confirm_multi_quotations/era_confirm_multi_quotations/objects/<model("era_confirm_multi_quotations.era_confirm_multi_quotations"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('era_confirm_multi_quotations.object', {
#             'object': obj
#         })

