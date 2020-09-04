"""Collect statistics about the music collection."""

import os
import matplotlib.pyplot as plt

def get_band_list(music_collection_path):
	'''Create a list of all band folders which are contained in the
	music collection. Folders which contain subgenres are expected to
	begin with a "#".
	'''
	bands = []
	for dirpath, subdirs, _ in os.walk(music_collection_path):
		# Create list of genres
		if dirpath == music_collection_path:
			genres = subdirs

		# Append bandnames to bands and subgenrenames to genres
		foldername = dirpath.split('/')[-1]
		if foldername in genres:
			for subdir in subdirs:
				if subdir[0] == '#':
					genres.append(subdir)
				else:
					bands.append(subdir)
	return bands

def get_dict_of_years(music_collection_path, bands):
	'''Create a dict which groups the albums of the music collection by
	years.
	'''
	d = {}
	for dirpath, subdirs, _ in os.walk(music_collection_path):
		for subdir in subdirs:
			folders_in_subdir = subdir.split()
			foldername = dirpath.split('/')[-1]
			
			if foldername in bands and folders_in_subdir[0][0] in ['1', '2']:
				# Check if the path points to a band folder and if the
				# subdir begins with a year; then append to the corres-
				# ponding year in d.
				year = int(folders_in_subdir[0])
				if year not in d:
					d[year] = []
				d[year].append(subdir)
	return d

def histo(d, bands, x='x', y='y', titel=''):
	'''Use ``d`` to make a histogram and plot it.'''
	list_of_years = []
	check = {}
	
	for year in d:
		for item in range(len(d[year])):
			# Add the year of every album to list_of_years
			list_of_years.append(year)
		
		check[year] = len(d[year])
	print('\ncheck histo:')
	for item in check:
		print(item,'-',check[item])
	
	zeitraum = max(list_of_years) - min(list_of_years)
	print(len(check), 'Eintraege in einem Zeitraum von', zeitraum, 'Jahren\n')
	print(len(bands), 'Bands und', len(list_of_years), 'Alben erfasst\n')
	print(list_of_years, '\n')

	plt.hist(list_of_years, zeitraum+1)
	plt.xlabel(x)
	plt.ylabel(y)
	plt.title(titel)