from odoo import models, fields, api
from odoo.exceptions import UserError
import base64
import logging

_logger = logging.getLogger(__name__)

class Internship(models.Model):
    _name = 'stage.internship'
    _description = 'Stage en entreprise'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    
    name = fields.Char(string='Titre du stage', required=True, tracking=True)
    description = fields.Text(string='Description', tracking=True)
    
    student_id = fields.Many2one('stage.student', string='Étudiant', required=True, tracking=True)
    company_id = fields.Many2one('stage.company', string='Entreprise', required=True, tracking=True)
    academic_tutor_id = fields.Many2one(
        'stage.tutor', string='Tuteur académique',
        domain=[('type', '=', 'academic')], tracking=True
    )
    professional_tutor_id = fields.Many2one(
        'stage.tutor', string='Tuteur professionnel',
        domain=[('type', '=', 'professional')], tracking=True
    )
    
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
        """Génère la convention de stage au format PDF (Standard Odoo - Search Workaround with Logging)"""
        self.ensure_one()
        report = None # Initialize report variable
        
        try:
            # --- Workaround: Search for the report action instead of using env.ref() --- 
            report_qweb_template_name = 'stage_management.report_internship_agreement'
            _logger.info(f"Searching for ir.actions.report with report_name = '{report_qweb_template_name}'")
            report = self.env['ir.actions.report'].search([
                ('report_name', '=', report_qweb_template_name)
            ], limit=1)

            if not report:
                _logger.warning(f"Search FAILED to find report action with report_name '{report_qweb_template_name}'.")
                # Attempt env.ref as a fallback
                try:
                    report_ref_str = 'stage_management.internship_agreement_report'
                    _logger.warning(f"Falling back to env.ref('{report_ref_str}')")
                    report = self.env.ref(report_ref_str)
                    _logger.info(f"Fallback env.ref succeeded for '{report_ref_str}'. Report object: {report}")
                except Exception as ref_err:
                    _logger.error(f"Fallback env.ref also FAILED for '{report_ref_str}': {ref_err}")
                    raise UserError(f"Impossible de trouver l'action de rapport associée au template '{report_qweb_template_name}' par recherche ou par référence. Vérifiez si le rapport est correctement défini et enregistré.")
            else:
                _logger.info(f"Search SUCCEEDED. Found report action: {report} with ID: {report.id}")
            # --- End Workaround --- 

            # Use Odoo's standard PDF generation
            _logger.info(f"Attempting to render PDF using report object: {report} (ID: {report.id if report else 'N/A'}) for docids: {self.ids}")
            pdf_content, content_type = report._render_qweb_pdf(self.ids)
            _logger.info(f"PDF rendering successful. Content type: {content_type}")

            if content_type != 'application/pdf':
                 _logger.error(f"Generated report content type is not PDF: {content_type}")
                 raise UserError("Le rapport généré n'est pas un PDF.")

            # Store PDF in the record
            _logger.info("Storing generated PDF in the record.")
            self.write({
                'agreement_generated': True,
                'agreement_file': base64.b64encode(pdf_content),
                'agreement_filename': f"Convention_Stage_{self.student_id.name}_{self.company_id.name}.pdf",
                'state': 'in_progress' if self.state == 'draft' else self.state
            })
            _logger.info("PDF stored successfully.")

            # Return URL action to download the PDF
            url = f"/web/content/stage.internship/{self.id}/agreement_file/{self.agreement_filename}?download=true"
            _logger.info(f"Returning download URL action: {url}")
            return {
                'type': 'ir.actions.act_url',
                'url': url,
                'target': 'self',
            }

        except Exception as e:
            _logger.error(f"Error in action_generate_agreement: {e}", exc_info=True) # Log full traceback
            # Log details about the report object at the time of error
            try:
                _logger.error(f"Error occurred with report object: {report} (Type: {type(report)}) during exception.")
            except:
                 _logger.error("Could not log report object details during exception.")
            raise UserError(f"Impossible de générer la convention standard. Erreur: {e}")
    
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

    def action_view_reports(self):
        """Ouvre la vue des rapports liés à ce stage"""
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Rapports',
            'view_mode': 'tree,form',
            'res_model': 'stage.report',
            'domain': [('internship_id', '=', self.id)],
            'context': {'default_internship_id': self.id}
        }

