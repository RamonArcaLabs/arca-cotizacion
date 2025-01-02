{
    'name': 'Cotización ArcaLabs',
    'version': '1.0',
    'author': 'Ramon Reyna',
    'category': 'Sales',
    'depends': ['sale', 'base', 'sale_management'],
    'data': [
        'security/ir.model.access.csv',
        'views/sale_order_views.xml',
        'views/sale_order_form.xml',
        'views/sale_order_lines.xml',
        'views/sale_order_template_form.xml',
        'reports/custom_quotation_template.xml',
        'reports/report_action.xml',
        'reports/products.xml',
        'data/data.xml',
        'data/automation.xml'
    ],
    'installable': True,
    'application': False,
}
