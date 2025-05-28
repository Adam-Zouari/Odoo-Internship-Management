from odoo import models, fields, api

class Student(models.Model):
    _name = 'stage.student'
    _description = 'Étudiant en stage'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    
    name = fields.Char(string='Nom', required=True, tracking=True)
    first_name = fields.Char(string='Prénom', required=True, tracking=True)
    email = fields.Char(string='Email', required=True, tracking=True)
    program = fields.Char(string='Filière', required=True, tracking=True)
    level = fields.Selection([
        ('l1', 'Licence 1'),
        ('l2', 'Licence 2'),
        ('l3', 'Licence 3'),
        ('m1', 'Master 1'),
        ('m2', 'Master 2'),
        ('doc', 'Doctorat'),
    ], string='Niveau', required=True, tracking=True)
    
    internship_ids = fields.One2many('stage.internship', 'student_id', string='Stages')
    internship_count = fields.Integer(compute='_compute_internship_count', string='Nombre de stages')
    
    @api.depends('internship_ids')
    def _compute_internship_count(self):
        for student in self:
            student.internship_count = len(student.internship_ids)

    def action_view_internships(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Stages',
            'view_mode': 'tree,form',
            'res_model': 'stage.internship',
            'domain': [('student_id', '=', self.id)],
            'context': {'default_student_id': self.id}
        }

    # --- Ajout de name_get pour afficher Prénom Nom ---
    def name_get(self):
        result = []
        for student in self:
            name = f"{student.first_name or ''} {student.name or ''}".strip()
            result.append((student.id, name))
        return result
    # --- Fin de name_get ---

