# import  frappe
# @frappe.whitelist(allow_guest=True)
# def fuc():
#     return {
#         "value": count,
#         "fieldtype": "Int",
#         "route": ["query-report", "Permitted Documents For User"]
#     }
from __future__ import unicode_literals
import frappe

@frappe.whitelist(allow_guest=True)
def fuc():
    # Get the count of assignments
    data = frappe.get_all("Assignment")
    count = len(data)
    # Create a JSON object with the count and route options
    return {
        "value": count,
        "fieldtype": "Int",
        "route_options": {"from_date": "2023-05-23"},
        # "route": ["query-report", "Permitted Documents For User"]
    }