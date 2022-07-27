import td

class MovieListExtenion:
	"""
	GuiExtension description
	"""
	def __init__(self, ownerComp):
		# The component to which this extension is attached
		self._owner_comp: td.baseCOMP = ownerComp
		self._table: td.tableDAT = op('table1')
		self._movie_bin: td.baseCOMP = op('../movie_bin')
		self._movie_bin.MovieCount.callbacks.append(self.onMovieCountChange)

	def __del__(self):
		self._movie_bin.MovieCount.callbacks.remove(self.onMovieCountChange)

	def onMovieCountChange(self, data: dict):
		self._table.clear(keepFirstRow=True)
		for movie in self._movie_bin.MovieList.val:
			self._table.appendRow([movie])

