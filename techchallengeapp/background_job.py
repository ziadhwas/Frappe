import frappe


def remove_rejected_candidates():
    frappe.sql("DELETE FROM `tabcandidate` WHERE `status` = 'rejected';")
