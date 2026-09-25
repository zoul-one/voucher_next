import frappe
import os

from frappe import _
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields
from voucher_next.custom.custom_field.journal_entry import get_journal_entry_custom_fields


def after_install():
    # Create Voucher Next specific custom fields
    create_custom_fields(get_custom_fields(), ignore_validate=True)

    # Create Voucher Next specific roles
    create_custom_roles(get_voucher_next_roles())


def after_migrate():
    # Create Voucher Next specific roles
    create_custom_roles(get_voucher_next_roles())

    # Run common setup
    after_install()


def before_uninstall():
    delete_custom_fields(get_custom_fields())


def get_voucher_next_roles():
    """
    Return Voucher Next specific roles.
    """
    return [

    ]


def get_custom_fields():
    """
    Return all Voucher Next specific custom fields.
    """

    custom_fields = {
        "Journal Entry": get_journal_entry_custom_fields(),
    }

    return custom_fields


def delete_custom_fields(custom_fields: dict):
    """
    Delete Voucher Next custom fields.

    Args:
        custom_fields: dict like:
            {
                "Voucher": [
                    {
                        "fieldname": "custom_example"
                    }
                ]
            }
    """

    for doctype, fields in custom_fields.items():
        frappe.db.delete(
            "Custom Field",
            {
                "fieldname": (
                    "in",
                    [field["fieldname"] for field in fields]
                ),
                "dt": doctype,
            },
        )

        frappe.clear_cache(doctype=doctype)


def create_custom_roles(roles):
    """
    Create Voucher Next specific roles.

    Args:
        roles: list of role names.
    """

    for role in roles:
        if not frappe.db.exists("Role", role):
            role_doc = frappe.get_doc(
                {
                    "doctype": "Role",
                    "role_name": role,
                }
            )

            role_doc.insert(ignore_permissions=True)

    frappe.db.commit()