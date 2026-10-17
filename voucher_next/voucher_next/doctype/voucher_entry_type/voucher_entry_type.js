// Copyright (c) 2026, Zoul Technologies Private Limited and contributors
// For license information, please see license.txt

frappe.ui.form.on('Voucher Entry Type', {
	setup: function(frm) {
		frm.set_query('default_account', 'accounts', function(doc, cdt, cdn) {
			let row = locals[cdt][cdn];
			let filters = {
				is_group: 0
			};
			if (row.company) {
				filters.company = row.company;
			}
			return {
				filters: filters
			};
		});
	}
});
