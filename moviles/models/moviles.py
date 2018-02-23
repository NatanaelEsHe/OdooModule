from odoo import models, fields, api

class Moviles(models.Model):
    _name = 'moviles.moviles'
    idMov = fields.Char('id movil',required = True)
    idProv = fields.Char('Proveedor', required = True)
    nombre = fields.Char('Nombre', required = True)
    marca = fields.Char('Marca',required = True)
    modelo = fields.Char('Modelo',required = True)
    stock = fields.Char('Stock', required = True)
    precio = fields.Char('Precio', required = True)
    garantia = fields.Char('Garantia', required = True)
    pntMov = fields.Char('Puntos', required = True)