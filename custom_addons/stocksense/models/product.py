from odoo import models, fields

class StockSenseProduct(models.Model):
    _name = 'stocksense.product'
    _description = 'Inventory Product Catalog'

    name = fields.Char(string='Product Name', required=True)
    default_code = fields.Char(string='Internal Reference / SKU')
    detailed_type = fields.Selection([
        ('consu', 'Consumable'),
        ('product', 'Storable Product'),
        ('service', 'Service')
    ], string='Product Type', default='product', required=True)
    list_price = fields.Float(string='Sales Price', default=1.0)
    standard_price = fields.Float(string='Cost Price', default=0.0)
    qty_available = fields.Float(string='Quantity On Hand', default=0.0)
    min_stock_level = fields.Float(string='Reordering Min Level', default=5.0)
