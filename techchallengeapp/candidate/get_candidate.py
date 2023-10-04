import frappe
from frappe.utils import get_url
import json
import requests
from frappe.model.document import Document


class MyApis(Document):

    def Get_Candidates(self):
        candidate = frappe.db.sql(
            f"SELECT * FROM `tabCandidate` AS candidate WHERE candidate.name ='{self.name}'")
        return candidate

    def Add_Candidate(doc):
        candidate = frappe.new_doc("Candidate")
        candidate.name = doc.name
        candidate.email = doc.email
        candidate.experiance = doc.experiance
        candidate.status = doc.status
        candidate.insert()
        candidate.save()

    def Add_Candidate(doc, id):
        candidate = frappe.get_doc("Candidate", id)
        candidate.name = doc.name
        candidate.email = doc.email
        candidate.experiance = doc.experiance
        candidate.status = doc.status
        candidate.save()
