{
    'name': "auth_otp_reset",

    'summary': "OTP-based password reset for StockSense",

    'description': """
Replaces Odoo's default reset-password-by-link flow with a numeric
OTP sent to the user's email, which they must verify before setting
a new password.
    """,

    'author': "Jabez",
    'website': "https://github.com/Alexrosariyo319/stocksense",

    'category': 'Extra Tools',
    'version': '19.0.1.0.0',

    'depends': ['base', 'auth_signup', 'mail'],

    'data': [
        'security/ir.model.access.csv',
        'views/templates.xml',
    ],
}
