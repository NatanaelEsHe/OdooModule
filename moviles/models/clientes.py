from odoo import models, fields, api

class Clientes(models.Model):
    _name = 'moviles.clientes'
    idCli = fields.Char('id cliente',required = True)
    nombCli = fields.Char('Nombre cliente', required = True)
    tlfCli = fields.Char('Telefono', required = True)
    codPosCli = fields.Char('Codigo postal',required = True)
    dirCli = fields.Char('Direccion',required = False)
    fecAlta = fields.Char('Fecha alta', required = True)
    pntCli = fields.Char('Sistema de puntos', required = False)