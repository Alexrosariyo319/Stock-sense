{
    'name': 'StockSense',
   'version': '17.0.1.0.0',
   'license': 'LGPL-3',
    'summary': 'Modular Inventory Management System',
    'category': 'Inventory/Warehouse',
    'depends': ['base', 'web'],
    'data': [
        'views/product_views.xml',
        'views/dashboard_views.xml',
        'views/menu_views.xml',
    ],
    'installable': True,
    'application': True,
}
