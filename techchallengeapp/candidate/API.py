import frappe
from frappe.utils import get_url
import json
import requests
from frappe.model.document import Document


@frappe.whitelist()
def Get_Candidates(self):
    candidate = frappe.db.sql(
        f"SELECT * FROM `tabCandidate` AS candidate WHERE candidate.name ='{self.name}'")
    return candidate


@frappe.whitelist()
def Add_Candidate(doc):
    document = json.loads(doc)
    print(document)
    candidate = frappe.new_doc("Candidate")
    candidate.candidate_name = document['name']
    candidate.email = document['email']
    candidate.experiance = document['experiance']
    candidate.status = document['status']
    candidate.insert()
    candidate.save()


@frappe.whitelist()
def Edit_Candidate(doc, id):
    candidate = frappe.get_doc("Candidate", id)
    candidate.name = doc.name
    candidate.email = doc.email
    candidate.experiance = doc.experiance
    candidate.status = doc.status
    candidate.save()
