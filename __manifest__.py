{
    'name': 'Cotización ArcaLabs',
    'version': '1.0',
    'author': 'Ramon Reyna',
    'category': 'Sales',
    'depends': ['sale', 'base'],
    'data': [
        'views/sale_order_views.xml',
        'views/sale_order_form.xml',
        'views/sale_order_lines.xml',
        'reports/custom_quotation_template.xml',
        'reports/report_action.xml',
        'reports/products.xml'
    ],
    'installable': True,
    'application': False,
}
