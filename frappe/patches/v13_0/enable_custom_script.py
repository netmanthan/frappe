# Copyright (c) 2020, Sparrownova Technologies
# License: MIT. See LICENSE

import frappe


def execute():
	"""Enable all the existing Client script"""

	frappe.db.sql(
		"""
		UPDATE `tabClient Script` SET enabled=1
	"""
	)
