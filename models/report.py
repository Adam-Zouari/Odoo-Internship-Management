from odoo import models, fields, api

class Report(models.Model):
    _name = 'stage.report'
    _description = 'Rapport de stage'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    
    name = fields.Char(string='Titre du rapport', required=True, tracking=True)
    internship_id = fields.Many2one('stage.internship', string='Stage', required=True, tracking=True)
    student_id = fields.Many2one(related='internship_id.student_id', string='Étudiant', store=True)
    submission_date = fields.Date(string='Date de soumission', default=fields.Date.today, tracking=True)
    
    report_file = fields.Binary(string='Fichier du rapport', attachment=True, required=True)
    report_filename = fields.Char(string='Nom du fichier')
    
    state = fields.Selection([
        ('draft', 'Brouillon'),
        ('submitted', 'Soumis'),
        ('validated', 'Validé'),
        ('rejected', 'Rejeté'),
    ], string='Statut', default='draft', tracking=True)
    
    comments = fields.Text(string='Commentaires', tracking=True)
    
    def action_submit(self):
        """Soumet le rapport pour validation"""
        self.write({'state': 'submitted'})
        
        # Notification au tuteur académique
        if self.internship_id.academic_tutor_id:
            self.message_subscribe(partner_ids=[self.internship_id.academic_tutor_id.partner_id.id])
            self.message_post(
                body=f"Le rapport '{self.name}' a été soumis pour validation.",
                partner_ids=[self.internship_id.academic_tutor_id.partner_id.id]
            )
    
    def action_validate(self):
        """Valide le rapport"""
        self.write({'state': 'validated'})
    
    def action_reject(self):
        """Rejette le rapport"""
        self.write({'state': 'rejected'})
    
    def action_reset_to_draft(self):
        """Réinitialise le rapport à l'état brouillon"""
        self.write({'state': 'draft'})
