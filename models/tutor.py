from odoo import models, fields, api

class Tutor(models.Model):
    _name = 'stage.tutor'
    _description = 'Tuteur de stage'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    
    name = fields.Char(string='Nom', required=True, tracking=True)
    first_name = fields.Char(string='Prénom', required=True, tracking=True)
    email = fields.Char(string='Email', required=True, tracking=True)
    phone = fields.Char(string='Téléphone', tracking=True)
    type = fields.Selection([
        ('academic', 'Académique'),
        ('professional', 'Professionnel'),
    ], string='Type', required=True, tracking=True)
    
    # Champs spécifiques
    department = fields.Char(string='Département', tracking=True)
    company_id = fields.Many2one('stage.company', string='Entreprise', tracking=True)
    position = fields.Char(string='Poste', tracking=True)
    
    internship_academic_ids = fields.One2many('stage.internship', 'academic_tutor_id', string='Stages (Académique)')
    internship_professional_ids = fields.One2many('stage.internship', 'professional_tutor_id', string='Stages (Professionnel)')
    internship_count = fields.Integer(compute='_compute_internship_count', string='Nombre de stages')
    
    @api.depends('internship_academic_ids', 'internship_professional_ids')
    def _compute_internship_count(self):
        for tutor in self:
            tutor.internship_count = len(tutor.internship_academic_ids) + len(tutor.internship_professional_ids)
            
    def action_view_internships(self):
        self.ensure_one()
        domain = [('academic_tutor_id', '=', self.id)]
        if self.type == 'professional':
            domain = [('professional_tutor_id', '=', self.id)]
            
        return {
            'type': 'ir.actions.act_window',
            'name': 'Stages',
            'view_mode': 'list,form',
            'res_model': 'stage.internship',
            'domain': domain,
            'context': {'default_academic_tutor_id' if self.type == 'academic' else 'default_professional_tutor_id': self.id}
        }

    # --- Ajout de name_get pour afficher Prénom Nom ---
    def name_get(self):
        result = []
        for tutor in self:
            name = f"{tutor.first_name or ''} {tutor.name or ''}".strip()
            result.append((tutor.id, name))
        return result
    # --- Fin de name_get ---

