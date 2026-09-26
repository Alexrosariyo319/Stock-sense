{
    'name': 'StockSense',
    'version': '17.0.1.0.0',
    'summary': 'Modular Inventory Management System',
    'category': 'Inventory/Warehouse',
    'license': 'LGPL-3',
    'depends': ['base', 'web'],
    'data': [
        'security/ir.model.access.csv',
        'views/product_views.xml',
        'views/dashboard_views.xml',
        'views/menu_views.xml',
    ],
    'installable': True,
    'application': True,
}
