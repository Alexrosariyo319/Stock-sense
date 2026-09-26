# from odoo import models, fields, api


# class auth_otp_reset(models.Model):
#     _name = 'auth_otp_reset.auth_otp_reset'
#     _description = 'auth_otp_reset.auth_otp_reset'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

