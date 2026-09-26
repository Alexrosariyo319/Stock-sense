import random
from datetime import timedelta

from odoo import models, fields, api


class AuthOtp(models.Model):
    _name = 'auth.otp'
    _description = 'One-Time Password for password reset'

    user_id = fields.Many2one('res.users', required=True, ondelete='cascade')
    code = fields.Char(required=True)
    expiry = fields.Datetime(required=True)
    is_used = fields.Boolean(default=False)

    @api.model
    def generate_otp(self, user):
        """Create a new OTP for the given user and email it to them."""
        code = str(random.randint(100000, 999999))
        expiry = fields.Datetime.now() + timedelta(minutes=10)

        otp = self.create({
            'user_id': user.id,
            'code': code,
            'expiry': expiry,
        })

        user.partner_id.message_post(
            body=f"Your password reset code is: {code}. It expires in 10 minutes.",
            subject="Your StockSense Password Reset Code",
            partner_ids=[user.partner_id.id],
        )
        return otp

    @api.model
    def verify_otp(self, user, code):
        """Check if a code is valid, unused, and unexpired for this user."""
        otp = self.search([
            ('user_id', '=', user.id),
            ('code', '=', code),
            ('is_used', '=', False),
        ], order='create_date desc', limit=1)

        if not otp or otp.expiry < fields.Datetime.now():
            return False

        otp.is_used = True
        return True
