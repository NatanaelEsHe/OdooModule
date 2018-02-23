from odoo import models, fields

class Ventas(models.Model):
    _name = 'moviles.ventas'
    idVen = fields.Char('id venta',required = True)
    idCli = fields.Char('id cliente', required = True)
    fecVenta = fields.Char('Fecha venta', required = True)