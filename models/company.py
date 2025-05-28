from odoo import models, fields, api

class Company(models.Model):
    _name = 'stage.company'
    _description = 'Entreprise partenaire'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    
    name = fields.Char(string="Nom de l'entreprise", required=True, tracking=True)
    contact_name = fields.Char(string='Nom du contact', tracking=True)
    contact_email = fields.Char(string='Email du contact', tracking=True)
    contact_phone = fields.Char(string='Téléphone du contact', tracking=True)
    sector = fields.Char(string="Secteur d'activité", tracking=True)
    address = fields.Text(string='Adresse', tracking=True)
    
    internship_ids = fields.One2many('stage.internship', 'company_id', string='Stages')
    internship_count = fields.Integer(compute='_compute_internship_count', string='Nombre de stages')
    
    @api.depends('internship_ids')
    def _compute_internship_count(self):
        for company in self:
            company.internship_count = len(company.internship_ids)

    # --- Méthode ajoutée pour le bouton "Stages" ---
    def action_view_internships(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Stages',
            'view_mode': 'tree,form',
            'res_model': 'stage.internship',
            'domain': [('company_id', '=', self.id)],
            'context': {'default_company_id': self.id}
        }
    # --- Fin de la méthode ajoutée ---

