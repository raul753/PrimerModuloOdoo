# -*- coding: utf-8 -*-
{
    'name': "pizzeria",

    'summary': """
        Módulo para tener un listado de los productos, las ventas y los empleados que las realizan""",

    'description': """
        Módulo simple que relaciona los productos que se vende el personal y las ventas que se hace de cada producto.
    """,

    'author': "Raúl",
    'website': "http://www.PizzaASIR.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
