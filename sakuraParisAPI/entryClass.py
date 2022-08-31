class Entry:
	def __init__ (self, heading, definition, page, offset):
		self._heading = heading
		self._definition = definition
		self._page = page
		self._offset = offset

	def getHeading(self):
		return self._heading

	def getDefinition(self):
		return self._definition

	def getPage(self):
		return self._page

	def getOffset(self):
		return self._offset