frappe.pages["candidates-data"].on_page_load = function (wrapper) {
  var page = frappe.ui.make_app_page({
    parent: wrapper,
    title: "None",
    single_column: true,
  });

  page.set_tite("Canditates Data");
};
