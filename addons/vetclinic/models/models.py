# -*- coding: utf-8 -*-

from odoo import models, fields, api

class vetclinic_animal(models.Model):
    _name = 'vetclinic.animal'

    name = fields.Char('Name', size=64)
    birthdate = fields.Date('Birthdate')
    classification_id = fields.Many2one('vetclinic.classification','Classification')
    breed_id = fields.Many2one('vetclinic.breed','Breed')
    label_ids = fields.Many2many('vetclinic.label','rel_animal_label','animal_id','label_id','Labels')
    history = fields.Text('History')
    res_partner_id = fields.Many2one('res.partner','Owner')
    image = fields.Binary('Image')


class vetclinic_res_partner(models.Model):
    _inherit = 'res.partner'
    animal_ids = fields.One2many('vetclinic.animal', 'res_partner_id', string="Pets")
 

class vetclinic_classification(models.Model):
    _name = 'vetclinic.classification'

    name = fields.Char('Name', size=32)
    breed_ids = fields.One2many('vetclinic.breed', 'classification_id', string="Breeds")

class vetclinic_breed(models.Model):
    _name = 'vetclinic.breed'

    name = fields.Char('Name', size=32)
    classification_id = fields.Many2one('vetclinic.classification','Classfication')

class vetclinic_labels(models.Model):
    _name = 'vetclinic.label'

    name = fields.Char('Name', size=32)   


 
