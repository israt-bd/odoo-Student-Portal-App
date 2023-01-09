# -*- coding: utf-8 -*-

from odoo import models,fields, api


class StudentPortal(models.Model):
    _name = 'student.portal'
    _description = 'Student Portal'

    image = fields.Image(string='Profile Picture')
    name = fields.Char(string='Name')
    _id = fields.Char(string='ID')
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    _address = fields.Char(string='Address')
    blood = fields.Char(string='Blood Group')

