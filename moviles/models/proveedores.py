from odoo import models, fields

class Proveedores(models.Model):
    _name = 'moviles.proveedores'
    idProv = fields.Char('id proveedor',required = True)
    nombProv = fields.Char('Nombre proveedor', required = True)
    tlfProv = fields.Char('Telefono de contacto', required = True)