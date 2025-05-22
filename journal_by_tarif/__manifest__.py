{
    'name': 'Journal Restriction by Tarif',
    'version': '16.0.1.0.5',
    'author': 'Gauchocode',
    'license': 'GPL-3',
    'category': 'Warehouse',
    'depends': ['base', 'sale', 'product', 'account'],
    'data': [
        'views/product_pricelist_view.xml',
        'views/account_move_view.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}