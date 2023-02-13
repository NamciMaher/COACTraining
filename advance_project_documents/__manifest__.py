# See LICENSE file for full copyright and licensing details.

{
    'name': 'Add the attachments project in Documents App',
    'version': '15.0.1.0.0',
    'category': 'Productivity/Documents',
    'author': 'Optimal',
    'website': 'http://www.yourcompany.com',
    'summary': 'Add the attachments of Project/Tasks to the Documents App .',
    'depends': [
        'base','documents','documents_project'
    ],
    'data': [
        'views/res_config_settings.xml',
    ],

    'installable': True,
    'auto_install': False,
    'application': True,
}

