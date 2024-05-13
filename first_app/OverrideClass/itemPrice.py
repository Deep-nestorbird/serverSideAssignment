import frappe
from frappe.model.document import Document
class itemPrice(Document):
    def validate(self):
        frappe.msgprint("this  is override class")