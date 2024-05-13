
from __future__ import unicode_literals
import frappe

def get_data():
    return {
        "data": [
            {
                "type": "number_card",
                "name": "assignment_count",
                "value": frappe.call('first_app.first_app.doctype.assignment.assignment.get_assignment_count'),
                "label": "Total Assignments",
                "color": "blue"
            }
        ]
    }