{
    'name': 'Tarif Restriction by User',
    'version': '16.0.1.0.1',
    'summary': 'Restrics what tarif can be used by each user',
    'author': 'Gauchocode',
    'license': 'GPL-3',
    'category': 'Warehouse',
    'depends': ['base', 'sale', 'product'],
    'data': [
        'views/res_users_view.xml',
        'views/sale_order_view.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}