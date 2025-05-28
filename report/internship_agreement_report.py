from odoo import models, api

class InternshipAgreementReport(models.AbstractModel):
    _name = 'report.stage_management.report_internship_agreement'
    _description = 'Rapport de convention de stage'
    
    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env['stage.internship'].browse(docids)
        return {
            'doc_ids': docids,
            'doc_model': 'stage.internship',
            'docs': docs,
        }
