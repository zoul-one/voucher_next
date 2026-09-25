from frappe import _


def get_journal_entry_custom_fields():
    return [
        {
            "fieldname": "reference_voucher_entry",
            "fieldtype": "Link",
            "label": _("Reference Voucher Entry"),
            "options": "Voucher Entry",
            "insert_after": "cheque_date",
        }
    ]