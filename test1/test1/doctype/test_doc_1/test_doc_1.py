# -*- coding: utf-8 -*-
# Copyright (c) 2018, DSL and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document


class Testdoc1(Document):
	
	def validate(self):
		#frappe.msgprint("Block and Level already exist")
		frappe.msgprint("your message msgprint",raise_exception=True)
		