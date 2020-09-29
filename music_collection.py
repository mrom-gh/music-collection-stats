"""Provides the MusicCollection class which represents a music
collection and includes statistical methods for analyzing the
collection.
"""

import os, re
import matplotlib.pyplot as plt

class MusicCollection:
	def __init__(self, music_collection_path):
		self.music_collection_path = music_collection_path
		self.paths = []
		self.list_of_years = []
		self.dict_of_years = {}

	def get_all_paths(self):
		for path, _, _ in os.walk(self.music_collection_path):
			self.paths.append(path)

	def get_list_of_years(self):
		r = re.compile(r'([1-2][0-9]{3}).*$')  # .../.../1994 ...
		matches = [r.findall(path) for path in self.paths]  # [None, ['1994 ...'], ...]
		self.list_of_years = sorted([int(match[0]) for match in matches if match])  # [1994, ...]

	def get_dict_of_years(self):
		for year in self.list_of_years:
			self.dict_of_years[year] = self.list_of_years.count(year)

	def fill(self):
		self.get_all_paths()
		self.get_list_of_years()
		self.get_dict_of_years()

	def plot_histo(self):
		x = list(self.dict_of_years.keys())
		y = [self.dict_of_years[key] for key in self.dict_of_years]
		print(type(x[0]))
		plt.hist(self.list_of_years, bins=1)
		plt.xlabel('Jahr')
		plt.ylabel('Anzahl Alben')
		plt.title('Anzahl Alben pro Jahr')
		plt.show()