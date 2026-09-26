# from odoo import http


# class AuthOtpReset(http.Controller):
#     @http.route('/auth_otp_reset/auth_otp_reset', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/auth_otp_reset/auth_otp_reset/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('auth_otp_reset.listing', {
#             'root': '/auth_otp_reset/auth_otp_reset',
#             'objects': http.request.env['auth_otp_reset.auth_otp_reset'].search([]),
#         })

#     @http.route('/auth_otp_reset/auth_otp_reset/objects/<model("auth_otp_reset.auth_otp_reset"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('auth_otp_reset.object', {
#             'object': obj
#         })

