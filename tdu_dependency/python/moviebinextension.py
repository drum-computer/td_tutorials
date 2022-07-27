import td
import tdu
import TDStoreTools
from os import listdir
from os.path import isfile, join

class MovieBinExtension:
	"""
	MovieBinExtension description
	"""
	def __init__(self, ownerComp):
		self._owner_comp: td.baseCOMP = ownerComp
		self._movie_list: tdu.Dependency = TDStoreTools.DependList()
		self._movie_count: tdu.Dependency = tdu.Dependency(0)


	@property
	def MovieList(self) -> tdu.Dependency:
		'''
		Returns a list of loaded movie names
		'''
		return self._movie_list

	@property
	def MovieCount(self) -> tdu.Dependency:
		'''
		Returns how many movies are currently loaded
		'''
		return self._movie_count

	def OnReadPressed(self):
		'''
		Callback for read button press
		'''
		movies_folder = self._owner_comp.par.Folder.eval()
		if not movies_folder:
			debug('no folder selected')
			return
		self._movie_list.val = [f for f in listdir(movies_folder) 
									if isfile(join(movies_folder, f))]
		self._movie_count.val = len(self._movie_list)

	def OnClearPressed(self):
		'''
		Callback for clear button press
		'''
		self._movie_list.val = []
		self._movie_count.val = 0

	def RenameItem(self, index, name):
		self._movie_list.val[index] = name
		self._movie_list.modified()