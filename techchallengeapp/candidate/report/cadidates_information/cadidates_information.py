# Copyright (c) 2023, ziad hwas and contributors
# For license information, please see license.txt

import frappe


query = """ SELECT * FROM `tabCandidate` AS candidates 
            WHERE candidates.docstatus <> 2
             """


def execute(filters=None):
    if not filters:
        filters = {}
    columns, data = [], []

    data = get_candidates_data(filters)
    columns = get_columns()

    return columns, data


def get_columns():
    return [

        {
            'fieldname': 'candidate_name',
            'label': 'Name',
            'fieldtype': 'Data',
        },
        {
            'fieldname': 'email',
            'label': 'Email',
            'fieldtype': 'Data',
            'width': '180',
        },
        {
            'fieldname': 'experience',
            'label': 'Experience',
            'fieldtype': 'Data',
            'width': '180',
        },
        {
            'fieldname': 'status',
            'label': 'Status',
            'fieldtype': 'Data',
            'width': '150',
        },
    ]


def get_candidates_data(filters):
    data_query = get_query(filters)
    print(data_query)
    data = frappe.db.sql(query, as_dict=True)
    return data


def get_conditions(filters):
    conditions = {}
    for key, value in filters.items():
        if filters.get(key):
            conditions[key] = value
    return conditions


def get_query(filters):
    query_filters = []
