import frappe
from frappe.utils import get_url
import json
import requests
from frappe.model.document import Document


class MyApis(Document):

    def GetCandidates(self):
        candidate = frappe.db.sql(
            f"SELECT * FROM `tabCandidate` AS candidate WHERE candidate.name ='{self.name}'")
        return candidate
