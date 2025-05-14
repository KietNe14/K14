from odoo import api, fields, models

class ResConfigSettings(models.TransientModel):
    group_powerbi_garage = fields.Boolean("PowerBI Garage", implied_group="project.group_project_stages")
    group_powerbi_attendance = fields.Boolean("PowerBI Attendance", implied_group="project.group_project_stages")