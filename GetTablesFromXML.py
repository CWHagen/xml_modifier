class GetTablesFromXML:
	"""docstring for GetTablesFromXML"""
	def __init__(self, parsed_xml_root):
		# super(GetTablesFromXML, self).__init__()
		self.parsed_xml_root = parsed_xml_root
		self.tables = parsed_xml_root.getElementsByTagName("table")

	def get_tables(self):
		for table_index, item in enumerate(self.tables, start=0):
			TableTrue = item.getAttribute('id')=='4B1C9DAC-CA97-42B0-8AF0-7388A8200FCA'
			if TableTrue:
			 	knoop_table_index = table_index
			 	self.knoop_table = self.tables[knoop_table_index]
			 	print "Node table found"
		
		for table_index, item in enumerate(self.tables, start=0):
			TableTrue = item.getAttribute('id')=='8BB4510B-F03B-441A-802E-BFD4853A2126'
			if TableTrue:
			 	support_node_table_index = table_index
			 	self.support_node_table = self.tables[support_node_table_index]
			 	print "Node support table found"
			# else:
			 	# print "Node support table not found"
		return self.support_node_table, self.knoop_table

		# for table_index, item in enumerate(self.tables, start=0):
		# 	TableTrue = item.getAttribute('id')=='08B8D2CD-198D-4EF1-9A42-518DB03E7989'
		# 	if TableTrue:
		# 	 	support_line_table_index = table_index
		# 	 	self.support_line_table = self.tables[support_line_table_index]
		# 	 	print "Line support table found"
		# return self.support_line_table




	