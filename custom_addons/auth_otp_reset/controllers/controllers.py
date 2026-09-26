from odoo import http
from odoo.http import request


class AuthOtpController(http.Controller):

    @http.route('/auth/otp/request', type='http', auth='public', methods=['GET', 'POST'], csrf=True)
    def request_otp(self, **kw):
        error = None
        if kw.get('login'):
            user = request.env['res.users'].sudo().search([('login', '=', kw['login'])], limit=1)
            if user:
                request.env['auth.otp'].sudo().generate_otp(user)
                return request.render('auth_otp_reset.otp_verify_page', {'login': kw['login']})
            else:
                error = "No account found with that email/login."
        return request.render('auth_otp_reset.otp_request_page', {'error': error})

    @http.route('/auth/otp/verify', type='http', auth='public', methods=['GET', 'POST'], csrf=True)
    def verify_otp(self, **kw):
        error = None
        login = kw.get('login')
        if kw.get('code') and kw.get('new_password'):
            user = request.env['res.users'].sudo().search([('login', '=', login)], limit=1)
            if user and request.env['auth.otp'].sudo().verify_otp(user, kw['code']):
                user.sudo().write({'password': kw['new_password']})
                return request.render('auth_otp_reset.otp_success_page', {})
            else:
                error = "Invalid or expired code. Please try again."
        return request.render('auth_otp_reset.otp_verify_page', {'login': login, 'error': error})
