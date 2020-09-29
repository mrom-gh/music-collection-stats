"""Provides the MusicCollection class which represents a music
collection and includes statistical methods for analyzing the
collection.
"""

# TODO: walk and append

import os, re
import matplotlib.pyplot as plt

class MusicCollection:
	def __init__(self, music_collection_path):
		self.music_collection_path = music_collection_path
		self.paths = []
		self.list_of_years = []
		self.dict_of_years = {}

	def get_all_paths(self):
		for path, dirs, files in os.walk(self.music_collection_path):
			paths.append(self.path)

	def get_list_of_years(self):
		r = re.compile(r'([1-2][0-9]{3}).*$')  # .../1994 ...
		matches = [r.findall(path) for path in self.paths]  # [None, ['1994 ...'], ...]
		self.list_of_years = [match[0] for match in matches if match]  # ['1994', ...]

	def get_dict_of_years(self):
		for year in self.list_of_years:
			self.dict_of_years[year] = self.list_of_years.count(year)

	def fill():
		self.get_all_paths()
		self.get_list_of_years()
		self.get_dict_of_years()

	def plot_histo(self):
		
		plt.bar(self.list_of_years, bins='auto')
		plt.show()