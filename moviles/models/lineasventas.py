from odoo import models, fields

class LineasVentas(models.Model):
    _name = 'moviles.lineasventas'
    idVen = fields.Char('id venta',required = True)
    idMov = fields.Char('id movil', required = True)
    cantidad = fields.Char('cantidad', required = True)