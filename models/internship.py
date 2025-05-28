from odoo import models, fields, api
from datetime import datetime

class Internship(models.Model):
    _name = 'stage.internship'
    _description = 'Stage en entreprise'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    
    name = fields.Char(string='Titre du stage', required=True, tracking=True)
    description = fields.Text(string='Description', tracking=True)
    
    student_id = fields.Many2one('stage.student', string='Étudiant', required=True, tracking=True)
    company_id = fields.Many2one('stage.company', string='Entreprise', required=True, tracking=True)
    academic_tutor_id = fields.Many2one('stage.tutor', string='Tuteur académique', 
                                        domain=[('type', '=', 'academic')], tracking=True)
    professional_tutor_id = fields.Many2one('stage.tutor', string='Tuteur professionnel', 
                                           domain=[('type', '=', 'professional')], tracking=True)
    
    start_date = fields.Date(string='Date de début', required=True, tracking=True)
    end_date = fields.Date(string='Date de fin', required=True, tracking=True)
    
    state = fields.Selection([
        ('draft', 'En attente'),
        ('in_progress', 'En cours'),
        ('completed', 'Terminé'),
        ('cancelled', 'Annulé'),
    ], string='Statut', default='draft', tracking=True)
    
    agreement_generated = fields.Boolean(string='Convention générée', default=False, tracking=True)
    agreement_file = fields.Binary(string='Fichier de convention', attachment=True)
    agreement_filename = fields.Char(string='Nom du fichier de convention')
    
    report_ids = fields.One2many('stage.report', 'internship_id', string='Rapports')
    report_count = fields.Integer(compute='_compute_report_count', string='Nombre de rapports')
    
    @api.depends('report_ids')
    def _compute_report_count(self):
        for internship in self:
            internship.report_count = len(internship.report_ids)
    
    def action_generate_agreement(self):
        """Génère la convention de stage au format PDF"""
        self.ensure_one()
        
        # Génération du PDF via le rapport Qweb
        report = self.env.ref('stage_management.internship_agreement_report')._render_qweb_pdf(self.ids)
        
        # Sauvegarde du PDF généré dans le champ binaire
        self.write({
            'agreement_generated': True,
            'agreement_file': base64.b64encode(report[0]),
            'agreement_filename': f"Convention_Stage_{self.student_id.name}_{self.company_id.name}.pdf",
            'state': 'in_progress' if self.state == 'draft' else self.state
        })
        
        # Retourne l'action pour télécharger ou prévisualiser (optionnel)
        return self.env.ref('stage_management.internship_agreement_report').report_action(self)
    
    def action_start_internship(self):
        """Démarre le stage"""
        self.write({'state': 'in_progress'})
    
    def action_complete_internship(self):
        """Termine le stage"""
        self.write({'state': 'completed'})
    
    def action_cancel_internship(self):
        """Annule le stage"""
        self.write({'state': 'cancelled'})
    
    def action_reset_to_draft(self):
        """Réinitialise le stage à l'état brouillon"""
        self.write({'state': 'draft'})

    # --- Méthode ajoutée pour le bouton "Rapports" ---
    def action_view_reports(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Rapports',
            'view_mode': 'tree,form',
            'res_model': 'stage.report',
            'domain': [('internship_id', '=', self.id)],
            'context': {'default_internship_id': self.id}
        }
    # --- Fin de la méthode ajoutée ---

# Il faut importer base64 pour la génération de PDF
import base64

