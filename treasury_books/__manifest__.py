# -*- coding: utf-8 -*-
{
    'name': "Treasury Books",

    'summary': """
        Module for management of MDA's treasury books""",

    'description': """
        Module for management of MDA's treasury books in accordance with the law of the Federal Republic of Nigeria
    """,

    'author': "MgB Computers",
    'website': "http://www.mgbcomputers.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','account_accountant'],

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