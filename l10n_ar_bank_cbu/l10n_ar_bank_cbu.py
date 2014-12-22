# -*- coding: utf-8 -*-
from openerp.osv import fields, osv


class Bank(osv.osv):
    _inherit = 'res.partner.bank'
    _columns = {
        'cbu': fields.integer('CBU',
                              help="Key Bank Uniform"),
    }
