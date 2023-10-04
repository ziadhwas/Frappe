frappe.pages["candidates-data"].on_page_load = function (wrapper) {
  var page = frappe.ui.make_app_page({
    parent: wrapper,
    title: "None",
    single_column: true,
  });

  page.set_title("Canditates Data");
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
          fieldname: "experiance",
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
        frappe.call({
          method: "techchallengeapp.candidate.API.Add_Candidate",
          args: {
            doc: values,
          },
          callback: function (r) {},
        });

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
};
