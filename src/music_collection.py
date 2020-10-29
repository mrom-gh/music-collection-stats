"""Provides the MusicCollection class which represents a music
collection and includes statistical methods for analyzing it.
"""

import os, re
import matplotlib.pyplot as plt

class MusicCollection:
	def __init__(self, music_collection_path):
		self.music_collection_path = music_collection_path
		self.paths = []
		self.years = []

	def _get_paths(self):
		for path, _, _ in os.walk(self.music_collection_path):
			self.paths.append(path)

	def _get_years(self):
		contains_year = re.compile(r'([1-2][0-9]{3}).*$')  # .../.../(1994) ...
		matches = [contains_year.findall(path) for path in self.paths]  # [None, ['1994'], ...]
		self.years = sorted(  # [1994, ...]
				[int(match[0]) for match in matches if match]
			)

	def fill(self):
		self._get_paths()
		self._get_years()

	def plot_histo(self):
		zeitraum = max(self.years) - min(self.years)
		plt.hist(self.years, zeitraum+1)
		plt.xlabel('Jahr')
		plt.ylabel('Anzahl Alben')
		plt.title('Anzahl Alben pro Jahr')
		plt.show()