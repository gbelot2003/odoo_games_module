# -*- coding: utf-8 -*-
{
    'name': "games_register",

    'summary': """
        Registro simple de juegos para conocimiento general de odoo
        """,

    'description': """
        Este modulo esta construido con el proposito de instruir en la metodologìa de odoo para la creación de modulos y una forma de mantener 
        ejemplos a futuro, se espera tener vistas, formularos, reportes etc...
    """,

    'author': "Gerardo A Belot",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Test',
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