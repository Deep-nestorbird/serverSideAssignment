import frappe
from frappe import _
from frappe.model.document import Document

# Define your custom DocType class
class Assignment(Document):
    def validate(self):
        # Check if the checkbox is checked and both First Name and Last Name are filled
        if self.agree and self.first_name and self.last_name:
            # Set the Full Name field to the concatenation of First Name and Last Name
            self.full_name = f"{self.first_name} {self.last_name}"
        else:
            # If validation fails, raise an error
            frappe.throw("Please fill both First Name and Last Name and check the checkbox.")

    # Override the autoname method to define custom naming logic
    
    # Function to generate the name based on the 'full_name' field value
    def generate_name_from_field(self, full_name):
        # Implement your logic here to generate the name based on the 'full_name' field value
        # For example, you can concatenate a prefix with the 'full_name'
        return f"{full_name.replace('', '_')}"

# Add this line to hook the customdoc class to the Custom DocType
# Replace 'my_custom_app.my_custom_app.doctype.customdoc.customdoc' with the correct path to your customdoc class
# For example, if your app is named 'my_app' and your module is named 'my_module', it would be 'my_app.my_module.doctype.customdoc.customdoc'


# Function to get customer details
@frappe.whitelist()
def get_customer_details(customer):
    customer_doc = frappe.get_doc('Customer', customer)
    data = {
        'from_lead': customer_doc.lead_name,
        'account_manager': customer_doc.account_manager,
        'customer_group': customer_doc.customer_group,
        'currency': customer_doc.default_currency,
        'price_list': customer_doc.default_price_list
    }
    return data

@frappe.whitelist(allow_guest=True)
def get_name_details(customer):
    customer_doc = frappe.get_doc('Customer', customer)
    data = {
       'customer_name': customer_doc.customer_name,
       'customer_group': customer_doc.customer_group
    }
    return data

def setup_route():
    return [
        {"method": "GET", "route": "/api/method/my_custom_app.my_custom_app.doctype.customdoc.customdoc.get_name_details", "handler": get_name_details}
]
# # @frappe.whitelist(allow_guest=True)
# # def create_customdoc(first_name, last_name, agree):
# #     try:
# #         # Convert agree_value to an integer (0 or 1)
# #         agree = int(agree)

# #         # Validate agree_value
# #         if agree not in (0, 1):
# #             return {"error": "agree_value must be 0 or 1"}

# #         # Create a new Custom Doc based on the received data
# #         customdoc = frappe.new_doc('Custom Doc')
# #         customdoc.first_name = first_name
# #         customdoc.last_name = last_name
# #         customdoc.agree = agree
# #         customdoc.insert()

# #         return {"message": "Custom Doc created successfully"}
# #     except Exception as e:
# #         return {"error": str(e)}

# # @frappe.whitelist(allow_guest=True)
# # def update_customdoc(docname, first_name):
# #     try:
# #         # Load the existing Custom Doc
# #         customdoc = frappe.get_doc('Custom Doc', docname)

# #         # Update the fields with the new values
# #         customdoc.first_name = first_name
# #         #customdoc.last_name = last_name

# #         # Convert agree_value to an integer (0 or 1)
# #         #agree = int(agree)

# #         # Validate agree_value
# #         #if agree not in (0, 1):
# #          #   return {"error": "agree_value must be 0 or 1"}

# #         #customdoc.agree = agree

# #         # Save the changes
# #         customdoc.save()

# #         return {"message": "Custom Doc updated successfully"}
# #     except Exception as e:
# #         return {"error": str(e)}
# # @frappe.whitelist(allow_guest=True)
# # def delete_customdoc(docname):
# #     try:
# #         # Load the existing Custom Doc
# #         customdoc = frappe.get_doc('Custom Doc', docname)

# #         # Delete the document
# #         customdoc.delete()

# #         return {"message": "Custom Doc deleted successfully"}
# #     except Exception as e:
# #         return {"error": str(e)}
    

# # from frappe.model.meta import get_meta
# # @frappe.whitelist(allow_guest=True)
# # def get_user_info_with_doctypes():
# #     try:
# #         # Get user doctypes
# #         user_doctypes = [d.name for d in frappe.get_all("DocType", filters={"module": "User"})]

# #         # Get user information
# #         user_info = frappe.get_all("User", fields=["full_name", "enabled", "name"])

# #         return {"user_doctypes": user_doctypes, "user_info": user_info}
# #     except Exception as e:
#         return {"error": str(e)}

# @frappe.whitelist(allow_guest=True)
# def create_user(email, full_name):
#     try:
#         # Create a new User
#         user = frappe.get_doc({
#             "doctype": "User",
#             "email": email,
#             "first_name": full_name,
#             #"custom_field": custom_field_value
#         })
#         user.insert(ignore_permissions=True)

#         return {"message": _("User created successfully")}
#     except Exception as e:
#         return {"error": str(e)}
# @frappe.whitelist()
# def get_custom_data():
#     # Implement your custom logic to fetch data
#     # For demonstration, let's return a sample data
#     return {
#         'total_sales': 1000,
#         'total_customers': 50,
#         'total_orders': 200
#     }
# from __future__ import unicode_literals
# import frappe

@frappe.whitelist()
def get_assignment_count():
    return frappe.db.count('Assignment', {'doctype': 'Assignment'})