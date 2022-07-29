import weakref
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
		self.c = weakref.ref(self.onMovieCountChange)
		self._movie_bin.MovieCount.callbacks.append(self.c)
		print("in init")

	def __del__(self):
		print("in del")
		self._movie_bin.MovieCount.callbacks.remove(self.c)

	def onMovieCountChange(self, data: dict):
		self._table.clear(keepFirstRow=True)
		for movie in self._movie_bin.MovieList.val:
			self._table.appendRow([movie])

