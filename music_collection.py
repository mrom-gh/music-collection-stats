"""Provides the MusicCollection class which represents a music
collection and includes statistical methods for analyzing the
collection.
"""

import os
import matplotlib.pyplot as plt

class MusicCollection:
	def __init__(self, music_collection_path):
		self.music_collection_path = music_collection_path
		self.genres = []
		self.bands = []
		self.dict_of_years = {}
	
	def walk_and_append(self, itemtype):
		# TODO
		for dirpath, subdirs, _ in os.walk(self.music_collection_path):
			foldername = dirpath.split('/')[-1]
			if foldername in self.genres:
				for subdir in subdirs:
					if subdir[0] == '#':
						self.genres.append(subdir)

	def get_genres(self):
		# Get main genres as subfolders of music_collection_path
		self.genres = next(os.walk(self.music_collection_path))[1]
		
		for dirpath, subdirs, _ in os.walk(self.music_collection_path):
			foldername = dirpath.split('/')[-1]
			if foldername in self.genres:
				for subdir in subdirs:
					if subdir[0] == '#':
						self.genres.append(subdir)
	
	def get_bands(self):
		'''Create a list of all band folders which are contained in the
		music collection. Subgenre folders are expected to start with
		a "#".
		'''
		for dirpath, subdirs, _ in os.walk(self.music_collection_path):
			foldername = dirpath.split('/')[-1]
			if foldername in self.genres:
				for subdir in subdirs:
					if subdir[0] != '#':
						self.bands.append(subdir)

	def get_dict_of_years(self):
		'''Create a dict which groups the albums of the music collection
		by years.
		'''
		for dirpath, subdirs, _ in os.walk(self.music_collection_path):
			for subdir in subdirs:
				folders_in_subdir = subdir.split()
				foldername = dirpath.split('/')[-1]
				
				if foldername in self.bands and folders_in_subdir[0][0] in ['1', '2']:
					# Check if the folder is a band folder and if the
					# subdir begins with a year; then append to the corres-
					# ponding year in dict_of_years.
					year = int(folders_in_subdir[0])
					if year not in self.dict_of_years:
						self.dict_of_years[year] = []
					self.dict_of_years[year].append(subdir)

	def fill(self):
		self.get_genres()
		self.get_bands()
		self.get_dict_of_years()
	
	def plot_histo(self):
		x = list(self.dict_of_years.keys())
		y = [len(self.dict_of_years[key]) for key in self.dict_of_years]
		plt.bar(x, y)
		plt.xlabel('Jahr')
		plt.ylabel('Anzahl Alben')
		plt.title('Anzahl Alben pro Jahr')
		plt.show()