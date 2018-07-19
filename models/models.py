# -*- coding: utf-8 -*-

from odoo import models, fields, api

class pedido(models.Model):
    _name = 'productos2.pedido'

    name = fields.Char(string="Nombre de pedido")
    foto_pedido = fields.Binary(string="Foto del pedido")
    fecha = fields.Date(string="Fecha en la que se realizó")
    telefono = fields.Char(string="Número de contacto", size=9)
    email = fields.Char(string="Email", default="@gmail.com")
    tipo = fields.Selection([('pizza','Pizza'),('bebida','Bebida'),('otro','Otro')], default="Género")
    localizacion = fields.Many2one('productos2.localizacion', string="localizacion")
    productito = fields.Many2one('productos2.producto', string="producto")

class localizacion(models.Model):
    _name = 'productos2.localizacion'

    name = fields.Char(string="Nombre de la calle")
    cod_postal = fields.Integer(string="codigo postal", size=5)
    localizacion_id = fields.One2many('productos2.pedido', 'localizacion', string="localizacion")

class personal(models.Model):
    _name = 'productos2.personal'

    name = fields.Char(string="Nombre del empleado")
    foto_empleado = fields.Binary(string="Foto")
    fecha_contratacion = fields.Date(string="Fecha de contratacion")
    telefono = fields.Char(string="Número de teléfono", size=9)
    dni = fields.Char(string="DNI", size=9)
    email = fields.Char(string="Email", default="@gmail.com")
    sexo = fields.Selection([('hombre','Hombre'),('mujer','Mujer'),('otro','Otro')], default="Género")
    asistio = fields.Many2one('productos2.asistencia', string="asistio")
    emple = fields.One2many('productos2.ventas', 'empleado', string="ventas")

class asistencia(models.Model):
    _name = 'productos2.asistencia'

    name = fields.Char(string="asistencia del empleado")
    cantidad = fields.Integer(string="horas trabajadas")
    asistencia_id = fields.One2many('productos2.personal', 'asistio', string="asistencia")

class ventas(models.Model):
    _name = 'productos2.ventas'

    name = fields.Char(string="Nombre del cliente")
    fecha_venta = fields.Date(string="Fecha de venta")
    producto = fields.Many2one('productos2.producto', string="producto")
    empleado = fields.Many2one('productos2.personal', string="empleado que lo vendio")

class producto(models.Model):
    _name = 'productos2.producto'

    name = fields.Char(string="Nombre del producto")
    foto_producto = fields.Binary(string="Foto")
    cantidad = fields.Integer(string="cantidad de productos")
    venta_id = fields.One2many('productos2.ventas', 'producto', string="ventas")
    product = fields.One2many('productos2.pedido', 'productito', string="cantidad de ventas")
