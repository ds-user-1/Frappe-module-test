# -*- coding: utf-8 -*-
# Copyright (c) 2018, DSL and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe import msgprint, _


class BinItem(Document):

	def validate(self):
		frappe.msgprint("BinItem your message msgprint",raise_exception=True)
		
