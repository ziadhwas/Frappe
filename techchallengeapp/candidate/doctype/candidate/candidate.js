// Copyright (c) 2023, ziad hwas and contributors
// For license information, please see license.txt

frappe.ui.form.on("Candidate", {
  // refresh: function(frm) {
  // }
});
let btn = page.set_primary_action("Create New Cabdidate", () =>
  frappe.prompt(
    [
      {
        label: "Candidate Name",
        fieldname: "name",
        fieldtype: "Data",
      },
      {
        label: "Candidate Email",
        fieldname: "email",
        fieldtype: "Data",
      },
      {
        label: "Experience",
        fieldname: "experience",
        fieldtype: "Data",
      },
      {
        fieldname: "status",
        fieldtype: "Select",
        label: "Status",
        options: "\nDraft\nShortlisted\nRejected\nHired",
      },
    ],
    (values) => {
      frappe.msgprint({
        title: __("Feedback"),
        indicator: "green",
        message: __(
          "Document updated successfully for candidate: " + values.name
        ),
      });
    }
  )
);
