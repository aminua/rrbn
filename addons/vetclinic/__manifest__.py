# -*- coding: utf-8 -*-
{
    'name': "Vet Clinic",

    'summary': """
        Vet Clinic Management Software
           

""",

    'description': """
        Module's purpose is to manage Vet Clinic Operations
         ---List Animals
	 --- List owners
         ---List breeds
    """,

    'author': "MgB Computers",
    'website': "http://www.mgbcomputers.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale_management'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
