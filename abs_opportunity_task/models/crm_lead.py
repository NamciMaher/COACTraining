from odoo import api,fields,models,_

class CrmLead(models.Model):
    _inherit = "crm.lead"

    task_count = fields.Integer(compute='_compute_task_count', string="Tasks Count")

    def _compute_task_count(self):
        count = 0
        task_ids = self.env['project.task'].search([])
        for record in self:
            if record.partner_id:
                for task_id in task_ids:
                    if record.partner_id == task_id.partner_id:
                        count=count+1 
                        record.task_count = count
                    else:
                        record.task_count = count
            else:
                record.task_count = count
        return True
